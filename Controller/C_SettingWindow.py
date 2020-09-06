from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from View.U_SettingWindow import Ui_SettingWindow


class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)