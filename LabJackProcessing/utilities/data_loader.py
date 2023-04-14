# load_data.py
import logging
import pandas as pd
from pathlib import Path

from LabJackProcessing.utilities.path_utilities import ensure_path_object

logger = logging.getLogger(__name__)

def load_data(file_path: Path) -> pd.DataFrame:
    file_path = ensure_path_object(file_path)
    logger.info(f"Opening {str(file_path)}...")
    
    rows_to_skip = 2  # Files from LabJack have a few nonconforming rows at the top that will mess with pandas
    file_extension = file_path.suffix.lower()
    
    if file_extension == ".csv":
        sep = ","
    elif file_extension in (".tsv", ".dat"):
        sep = "\t"
    else:
        logger.error(f"Unsupported file format: {file_extension}")
        return None

    df = pd.read_csv(file_path, sep=sep, skiprows=rows_to_skip)

    force_column_name = 'Force_in_kN'
    force_column_code = 'y2'
    alternate_force_column_code = 'y1'
    try:
        rename_column(df=df, old_column_name=force_column_code, new_column_name=force_column_name)
    except KeyError:
        rename_column(df=df, old_column_name=alternate_force_column_code, new_column_name=force_column_name)
    except:
        logger.error(f"Failed to find force column in file.")
        raise Exception("Failed to find force column in file.")

    return df

def rename_column(df: pd.DataFrame, old_column_name: str, new_column_name: str):
    if old_column_name in df.columns:
        logger.info(f"Renaming {old_column_name} to {new_column_name}...")
        df.rename(columns={old_column_name: new_column_name}, inplace=True)
    else:
        logger.error(f"Column {old_column_name} not found in file.")
        raise KeyError(f"Column {old_column_name} not found in file.")