# tab1.py
import logging
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QComboBox, QSizePolicy
from PyQt6.QtGui import QFontMetrics

from LabJackProcessing.gui.widgets.run_button_widget import RunButtonWidget


logger = logging.getLogger(__name__)

class BatchGraphTab(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self._layout)

        self.folder_open_button = QPushButton('Load a folder of files')
        self.folder_open_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.folder_open_button.setFixedSize(200, 40)
        self._layout.addWidget(self.folder_open_button)
        self.folder_open_button.clicked.connect(self._open_session_folder_dialog)

        self._path_to_folder_label = QLabel("No folder selected")
        self._layout.addWidget(self._path_to_folder_label)

        self.file_type_selector = QComboBox()
        self.file_type_selector.addItem(".dat")
        self.file_type_selector.addItem(".csv")
        self.file_type_selector.addItem(".tsv")
        self.file_type_selector.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.file_type_selector.setFixedSize(200, 40)
        self._layout.addWidget(self.file_type_selector)
        self.file_type_selector.currentIndexChanged.connect(self.get_selected_file_type)

        self.run_button = RunButtonWidget(self)
        self._layout.addWidget(self.run_button)

    def _open_session_folder_dialog(self):
        self._folder_path = QFileDialog.getExistingDirectory(None, "Choose a folder")
        if self._folder_path: 
            self._update_path_to_folder_label(self._folder_path)
            self.run_button.set_folder_path(Path(self._folder_path))
            self.run_button.run_button_widget.setEnabled(True)

    def get_selected_file_type(self):
        file_type = self.file_type_selector.currentText()
        logger.info(f"File type selected: {file_type}")
        self.run_button.set_file_type(file_type)

    def _update_path_to_folder_label(self, text):
        max_width = 400
        metrics = QFontMetrics(self._path_to_folder_label.font())
        elided_text = metrics.elidedText(text, Qt.TextElideMode.ElideMiddle, max_width)
        self._path_to_folder_label.setText(elided_text)
