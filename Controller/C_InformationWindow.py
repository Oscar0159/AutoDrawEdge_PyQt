from PyQt5.QtWidgets import QMainWindow

from View.U_InformationWindow import Ui_InformationWindow


class InformationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InformationWindow()
        self.ui.setupUi(self)