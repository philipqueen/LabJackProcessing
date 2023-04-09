import logging

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

from LabJackProcessing.gui.widgets.batch_graph_tab_widget import BatchGraphTab
from LabJackProcessing.gui.widgets.single_graph_tab_widget import SingleGraphTab

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        logger.info("Initializing the main window")
        super().__init__()

        self.setGeometry(100, 100, 600, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.batch_graph_tab = BatchGraphTab()
        self.tabs.addTab(self.batch_graph_tab, "Batch Graph Data Files")

        self.single_graph_tab = SingleGraphTab()
        self.tabs.addTab(self.single_graph_tab, "Graph Single Data File")

def run_gui_window():
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == "__main__":
    run_gui_window()
