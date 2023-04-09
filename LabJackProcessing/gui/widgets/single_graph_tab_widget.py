# tab2.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QSizePolicy
from PyQt6.QtCore import Qt
import pyqtgraph as pg

from LabJackProcessing.utilities.path_utilities import get_file_name
from LabJackProcessing.utilities.data_loader import load_data

class SingleGraphTab(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.file_open_button = QPushButton("Load a data file")
        self.file_open_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.file_open_button.setFixedSize(200, 40)
        self.file_open_button.clicked.connect(self._open_data_file_dialog)
        layout.addWidget(self.file_open_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self._path_to_file_label = QLabel("No file selected")
        layout.addWidget(self._path_to_file_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.plot_widget = pg.PlotWidget()

        self.plot_title = "Example Plot"
        self.plot_widget.setTitle(self.plot_title)
        self.plot_widget.setLabel('left', 'Force (kN)')
        self.plot_widget.setLabel('bottom', 'Time (s)')

        x_data = [0,1,2,3]
        y_data = [0,2,4,8]

        max_force_text = pg.TextItem(f"Max Force: 8 kN")
        self.plot_widget.addItem(max_force_text)

    
        self.plot_widget.plot(x_data, y_data)

        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def _open_data_file_dialog(self):
        options = QFileDialog.Option.ReadOnly
        file_filter = "Data files (*.dat *.csv *.tsv);;All files (*)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Open a data file", "", file_filter, options=options)

        if file_path:
            self._new_file_path_received(file_path)

    def _new_file_path_received(self, file_path):
        self._path_to_file_label.setText(file_path)

        self.input_dataframe = load_data(file_path)

        self.plot_title = get_file_name(file_path)
        self.plot_widget.setTitle(self.plot_title)

        self._update_plot(self.input_dataframe)

    def _update_plot(self, df):
        # Extract data
        x_data = df['Time']
        y_data = df['Force_in_kN']
        
        # Clear and update the plot
        self.plot_widget.clear()
        self.plot_widget.plot(x_data, y_data)
        max_force = y_data.max()
        max_force_text = pg.TextItem(f"Max Force: {max_force} kN")
        self.plot_widget.addItem(max_force_text)
        max_force_text.setPos(1, max_force)

