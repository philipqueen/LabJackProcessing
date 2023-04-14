import logging
import pandas as pd
import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters
from pathlib import Path

logger = logging.getLogger(__name__)

from LabJackProcessing.utilities.path_utilities import get_parent_directory, create_directory, get_file_name, ensure_path_object
from LabJackProcessing.utilities.file_search import find_files_in_folder
from LabJackProcessing.utilities.data_loader import load_data

def graph_folder_of_files(data_folder_path: Path, file_type: str):
    graph_folder_name = "graph_outputs"
    parent_directory = get_parent_directory(data_folder_path)
    graph_folder_path = create_directory(parent_directory=parent_directory, directory_name=graph_folder_name)

    file_list = find_files_in_folder(folder_path=data_folder_path, file_extension=file_type)

    for file in file_list:
        file_name = get_file_name(file)
        graph_name = file_name + ".jpg"
        graph_path = graph_folder_path / graph_name

        df = load_data(data_folder_path / file)

        # find max force
        max_force = df['Force_in_kN'].max()
        # index_of_max_force = df['Force_in_kN'].idxmax() #find the index where that max occurred
        # time_of_max_force = df['Time'][index_of_max_force] # get the time value for that index

        plot = create_plot(file_name=file_name, x_data=df['Time'], y_data=df['Force_in_kN'], max_force=max_force, file_destination=graph_path)

    logger.info("All done!")

def create_plot(file_name: str, x_data, y_data, max_force: float, file_destination: Path):
    # TODO add padding to plot like this: https://stackoverflow.com/questions/66119049/how-do-i-prevent-pyqtgraph-from-making-the-axis-larger-than-the-widget-size
    plot_title = f"{file_name}"

    plot_object = pg.plot(x_data, y_data)
    
    plot_object.setTitle(plot_title)
    plot_object.setLabel('left', 'Force (kN)')
    plot_object.setLabel('bottom', 'Time (s)')

    max_force_text = pg.TextItem(f"Max Force: {max_force} kN")
    plot_object.addItem(max_force_text)
    max_force_text.setPos(1, max_force)

    
    logger.info(f"Saving plot to {file_destination}")
    file_destination = ensure_path_object(file_destination)
    exporter = pyqtgraph.exporters.ImageExporter(plot_object.plotItem)

    exporter.parameters()['width'] = 1920

    exporter.export(str(file_destination))
    logger.info(f"Plot saved")
    plot_object.close()

if __name__ == "__main__":
    example_path = Path("YOUR/PATH/HERE")
    graph_folder_of_files(example_path)