from PyQt5.QtCore import Qt, QMetaObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit


class Ui_UrlWindow(object):
    def setupUi(self, MainWindow):
        # QMainWindow --------------------------------------
        MainWindow.resize(600, 25)
        MainWindow.setWindowTitle('Url')
        MainWindow.setFixedHeight(MainWindow.height())
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        MainWindow.setWindowIcon(QIcon('images/AutoDrawEdge.ico'))

        self.lineEdit = QLineEdit(MainWindow)
        self.lineEdit.setObjectName('lineEdit')

        MainWindow.setCentralWidget(self.lineEdit)


        QMetaObject.connectSlotsByName(MainWindow)

