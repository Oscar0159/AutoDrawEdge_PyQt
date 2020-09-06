from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QBitmap, QPixmap
from PyQt5.QtWidgets import QApplication


class Ui_CaptureWidget(object):
    def setupUi(self, Widget):
        # QWidget --------------------------------------
        Widget.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        Widget.setStyleSheet('''background-color:black; ''')
        Widget.setWindowOpacity(0.6)
        Widget.setGeometry(QRect(QApplication.desktop().pos(), QApplication.desktop().size()))
        Widget.setCursor(Qt.CrossCursor)