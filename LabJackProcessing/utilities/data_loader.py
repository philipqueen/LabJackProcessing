# load_data.py
import logging
import pandas as pd
from pathlib import Path

from LabJackProcessing.utilities.path_utilities import ensure_path_object

logger = logging.getLogger(__name__)

def load_data(file_path: Path):
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

    df.columns = ["Time", "Voltage1", "Voltage2", "Distance_Traveled", "Force_in_kN"]

    return df
