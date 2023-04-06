import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)

def get_parent_directory(path: Union[str, Path]) -> Path:
    path = ensure_path_object(path)

    logger.info(f"Input path: {path}")

    if path == path.parent:
        logger.warning(f"Root directory detected, no parent directory. Returning {path}")
        return path

    parent_directory = path.parent
    logger.info(f"Parent directory: {parent_directory}")

    return parent_directory

def create_directory(parent_directory: Path, directory_name: str) -> Path:
    """
    Create a new directory under the specified parent directory.
    
    Args:
        parent_directory (Union[str, Path]): The parent directory where the new directory will be created.
        directory_name (str): The name of the new directory.
        
    Returns:
        Path: The path of the created directory.
    """
    parent_directory = ensure_path_object(parent_directory)
    new_directory_path = parent_directory / directory_name

    try:
        new_directory_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {new_directory_path}")
    except Exception as e:
        logging.error(f"Error creating directory: {new_directory_path}. Exception: {e}")
        raise

    return new_directory_path

def ensure_path_object(path: Union[str, Path]) -> Path:
    """
    Ensure the input is a Path object. If the input is a string, convert it to a Path object.
    
    Args:
        path (Union[str, Path]): The input path as a string or a Path object.
    
    Returns:
        Path: The input path as a Path object.
    """
    if not isinstance(path, Path):
        path = Path(path)

    return path