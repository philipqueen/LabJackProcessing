import logging
from pathlib import Path
from glob import glob

logger = logging.getLogger(__name__)

def find_files_in_folder(folder_path: Path, file_extension: str) -> list:
    """
    Return a list of all video files in the base_path folder that match the given file type.
    file_type can be upper or lower case, with or without a leading period.
    This function is robust to the different behavior of glob on windows vs. mac/linux
    """

    # create general search from file type to use in glob search, including cases for upper and lowercase file types
    file_extension_upper = "*" + file_extension.upper()
    file_extension_lower = "*" + file_extension.lower()
    
    video_filepath_list = list(folder_path.glob(file_extension_upper)) + list(
        folder_path.glob(file_extension_lower)
    ) 
    # because glob behaves differently on windows vs. mac/linux, we collect all files both upper and lowercase, and remove redundant files that appear on windows
    unique_video_filepath_list = get_unique_list(video_filepath_list)

    logger.info(f"{len(unique_video_filepath_list)} videos found in folder")

    return unique_video_filepath_list

def get_unique_list(list: list) -> list:
    """Return a list of the unique elements from input list"""
    unique_list = []
    [unique_list.append(clip) for clip in list if clip not in unique_list]
    return unique_list