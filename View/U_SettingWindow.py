from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Ui_SettingWindow(object):
    def setupUi(self, MainWindow):
        # QMainWindow --------------------------------------
        MainWindow.resize(400, 600)
        MainWindow.setWindowTitle('Setting')
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        MainWindow.setWindowIcon(QIcon('images/AutoDrawEdge.ico'))