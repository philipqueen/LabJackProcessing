import logging

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

from LabJackProcessing.graph_folder_of_files import graph_folder_of_files


logger = logging.getLogger(__name__)
class RunButtonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self._layout = QVBoxLayout()

        self._title = QLabel(f"The code for this widget is defined in the file: {__file__}")
        self._layout.addWidget(self._title)
        
        self.run_button_widget = QPushButton('Run',self)
        self.run_button_widget.setEnabled(False)
        self._layout.addWidget(self.run_button_widget)

        self.run_button_widget.clicked.connect(self.run_script)

        self.setLayout(self._layout)

    def set_folder_path(self, folder_path):
        self._folder_path = folder_path

    def run_script(self):
        graph_folder_of_files(self._folder_path)