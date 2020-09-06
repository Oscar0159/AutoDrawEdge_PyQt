from PyQt5.QtGui import QIcon


class Ui_InformationWindow(object):
    def setupUi(self, MainWindow):
        # QMainWindow --------------------------------------
        MainWindow.resize(400, 300)
        MainWindow.setWindowTitle('Information')
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowIcon(QIcon('images/AutoDrawEdge.ico'))