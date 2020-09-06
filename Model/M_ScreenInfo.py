from PyQt5.QtCore import QRect, Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication


class ScreenInfoManager:
    def __init__(self):
        self._screenNum = QApplication.desktop().screenCount()
        self._screenPos = QApplication.desktop().pos()
        self._screenSize = QApplication.desktop().size()
        self._captureRegion = QRect()
        self._drawRegion = QRect()
        self._screenImg = QPixmap()

    def refreshScrInfo(self):
        self._screenNum = QApplication.desktop().screenCount()
        self._screenPos = QApplication.desktop().pos()
        self._screenSize = QApplication.desktop().size()

    def screenshot(self):
        self._screenImg = QPixmap(self._screenSize)
        self._screenImg.fill(Qt.black)
        painter = QPainter(self._screenImg)
        for index, screen in enumerate(QApplication.screens()):
            p = screen.grabWindow(0)
            offx = QApplication.desktop().pos().x()
            offy = QApplication.desktop().pos().y()
            x, y, w, h = screen.geometry().getRect()
            painter.drawPixmap(QPoint(x - offx, y - offy), p)

    def get_captureRegionImg(self) -> QPixmap:
        return self._screenImg.copy(self._captureRegion)

    def get_drawRegionImg(self) -> QPixmap:
        return self._screenImg.copy(self._drawRegion)

    @property
    def screenImg(self):
        return self._screenImg

    @property
    def captureRegion(self):
        return self._captureRegion

    @captureRegion.setter
    def captureRegion(self, new_captureRegion):
        self._captureRegion = new_captureRegion

    @property
    def drawRegion(self):
        return self._drawRegion

    @drawRegion.setter
    def drawRegion(self, new_drawRegion):
        self._drawRegion = new_drawRegion