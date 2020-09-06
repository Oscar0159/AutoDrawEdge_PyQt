import re

from PyQt5.QtCore import QRect, QRectF, Qt
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen
from PyQt5.QtWidgets import QLabel

from View.U_DLabel import Ui_DLabel

# image drag and drop label
class DLabel(QLabel):
    def __init__(self, parent=None):
        super(DLabel, self).__init__(parent=parent)
        self.ui = Ui_DLabel()
        self.ui.setupUi(self)

        self._dropQPixmap = QPixmap()
        self._resizeQPixmap = QPixmap()
        self._edgeQPixmap = QPixmap()

    def dragEnterEvent(self, e) -> None:
        file_name = e.mimeData().text()
        if file_name.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            e.acceptProposedAction()
        else:
            e.ignore()

    def dropEvent(self, e) -> None:
        file_path = e.mimeData().text()
        file_path = re.sub('file:///', '', file_path)
        print(file_path)
        self._dropQPixmap = QPixmap(file_path)


        if self._dropQPixmap.height() > self._dropQPixmap.width():
            self._resizeQPixmap = self._dropQPixmap.scaledToHeight(170)
            self.setPixmap(self._resizeQPixmap)
        else:
            self._resizeQPixmap = self._dropQPixmap.scaledToWidth(170)
            self.setPixmap(self._resizeQPixmap)
