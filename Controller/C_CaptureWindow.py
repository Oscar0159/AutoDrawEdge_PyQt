import numpy as np

from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QBrush, QBitmap, QPixmap, qRed, qGreen, qBlue
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from Model import M_AutoDraw
from View.U_CaptureWindow import Ui_CaptureWidget


def qtpixmap2cvimg(qpix: QPixmap):

    qimg = qpix.toImage()

    # 使用numpy建立空的圖象
    cv_image = np.zeros((qimg.height(), qimg.width(), 3), dtype=np.uint8)

    for row in range(0, qimg.height()):
        for col in range(0, qimg.width()):
            r = qRed(qimg.pixel(col, row))
            g = qGreen(qimg.pixel(col, row))
            b = qBlue(qimg.pixel(col, row))
            cv_image[row, col, 0] = b
            cv_image[row, col, 1] = g
            cv_image[row, col, 2] = r

    return cv_image


class CaptureWidget(QMainWindow):
    captureSignal = pyqtSignal(QRect)
    def __init__(self, parent=None):
        super(CaptureWidget, self).__init__(parent)
        self.ui = Ui_CaptureWidget()
        self.ui.setupUi(self)

        self._blackMask = QBitmap(QApplication.desktop().size())
        self._blackMask.fill(Qt.black)
        self._mask = self._blackMask.copy()
        self._isDrawing = False
        self._startPoint = QPoint()
        self._endPoint = QPoint()
        self._rect = QRect()

    def showEvent(self, e) -> None:
        self.clearMask()

    def hideEvent(self, e) -> None:
        pass

    def paintEvent(self, event):
        if self._isDrawing:
            self._mask = self._blackMask.copy()
            pp = QPainter(self._mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self._startPoint, self._endPoint))
            self.setMask(QBitmap(self._mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._startPoint = event.pos()
            self._endPoint = self._startPoint
            self._isDrawing = True

        elif event.button() == Qt.RightButton:
            self._endPoint = event.pos()
            self._isDrawing = False
            self.hide()

    def mouseMoveEvent(self, event):
        if self._isDrawing:
            self._endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self._isDrawing = False
        if event.button() == Qt.LeftButton:
            self._endPoint = event.pos()

            # First quadrant
            if self._endPoint.x() > self._startPoint.x() and self._endPoint.y() < self._startPoint.y():
                self._rect = QRect(self._startPoint.x(), self._endPoint.y(),
                             self._endPoint.x() - self._startPoint.x(), self._startPoint.y() - self._endPoint.y())
            # Second quadrant
            elif self._endPoint.x() < self._startPoint.x() and self._endPoint.y() < self._startPoint.y():
                self._rect = QRect(self._endPoint.x(), self._endPoint.y(),
                             self._startPoint.x() - self._endPoint.x(), self._startPoint.y() - self._endPoint.y())
            # Third quadrant
            elif self._endPoint.x() < self._startPoint.x() and self._endPoint.y() > self._startPoint.y():
                self._rect = QRect(self._endPoint.x(), self._startPoint.y(),
                             self._startPoint.x() - self._endPoint.x(), self._endPoint.y() - self._startPoint.y())
            # Fourth  quadrant
            else:
                self._rect = QRect(self._startPoint, self._endPoint)

            self.hide()

            self.captureSignal.emit(self._rect)
