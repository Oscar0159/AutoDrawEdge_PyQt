from PyQt5.QtCore import Qt, pyqtSlot, QMetaObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from View.U_UrlWindow import Ui_UrlWindow


class UrlWindow(QMainWindow):
    editFibisgedSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_UrlWindow()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        self.editFibisgedSignal.emit(self.ui.lineEdit.text())
