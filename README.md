# LabJack Processing
An easy to use graphical user interface (GUI)  to process data acquired from LabJack data acquisition systems, specifically focusing on load cell data. The code provided in this repository allows users to process data files with extensions .dat, .csv, or .tsv.

## Getting Started
To start using this repository, follow these steps:

1. Clone the repository or download it as a ZIP file and extract it to a folder on your computer.

2. Make sure you have Python installed on your system. If not, [here are instructions for downloading VSCode and using it with Python](https://code.visualstudio.com/docs/python/python-tutorial).

3. Install the required dependencies by opening a terminal (or command prompt) and navigating to the folder where you extracted the repository. Run the following command: `pip install -r requirements.txt`

4. After installing the required dependencies, you can start the GUI by running the following command in the terminal (or command prompt): `python __main__.py`

## Using the GUI
Once the GUI is open, choose either the "Batch Graph Data Files" or "Graph Single Data File" tab. The "Batch Graph Data Files" tab allows you to generate plots for a whole folder of data files at once, and automatically saves them to file.

The "Graph Single Data File" allows you to display any data file in an interactive plot.

By right clicking on the plot you can export the image, or perform analyses like downsampling the data.


## Contributing
If you'd like to contribute to the repository, feel free to open an issue or create a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
