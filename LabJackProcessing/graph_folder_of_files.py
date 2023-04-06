import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

logger = logging.getLogger(__name__)

from utilities.path_utilities import get_parent_directory, create_directory, get_file_name
from utilities.file_search import find_files_in_folder

def graph_folder_of_files(data_folder_path: Path, file_type: str):
    # create folder for graphs
    graph_folder_name = "graph_outputs"
    parent_directory = get_parent_directory(data_folder_path)
    graph_folder_path = create_directory(parent_directory=parent_directory, directory_name=graph_folder_name)

    file_list = find_files_in_folder(folder_path=data_folder_path, file_extension=file_type)

    # load and process all files coded file for testing
    for file in file_list:
        # create name and path for file
        file_name = get_file_name(file)
        graph_name = file_name + ".jpg"
        graph_path = graph_folder_path / graph_name

        # load csv data into pandas dataframe
        logger.info(f"Opening {file_name}...")
        rows_to_skip = 2 #files from lab jack have a few nonconforming rows at the top that will mess with pandas
        df = pd.read_csv(data_folder_path / file, sep='\t', skiprows = rows_to_skip)

        # set column names
        df.columns = ['Time', 'Voltage1', 'Voltage2', 'Distance_Traveled', 'Force_in_kN']

        # find max force
        max_force = df['Force_in_kN'].max()
        # index_of_max_force = df['Force_in_kN'].idxmax() #find the index where that max occurred
        # time_of_max_force = df['Time'][index_of_max_force] # get the time value for that index

        # create plot
        ax = df.plot(x = 'Time',
        y = 'Force_in_kN',)

        # add text giving max force info
        ax.text(0, (max_force * 0.8), f'Max Force is {max_force} kN', fontsize = 20)

        # remove legend and set label and title
        ax.get_legend().remove()
        ax.set_ylabel("Force in kN")
        ax.set_title(file_name)

        # save figure
        logger.info("Saving figure...")
        ax.figure.savefig(graph_path, dpi = 300)

        # clear matplotlib for next plot
        plt.cla()
        plt.clf()
        plt.close()


    logger.info("All done!")

if __name__ == "__main__":
    example_path = Path("YOUR/PATH/HERE")
    graph_folder_of_files(example_path)