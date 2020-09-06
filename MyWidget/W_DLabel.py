import re
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon


# drag and drop image label
class DLabel(QLabel):
    def __init__(self, parent=None):
        super(DLabel, self).__init__(parent=parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')

        self._dropQPixmap = QPixmap()
        self._resizeQPixmap = QPixmap()
        self._edgeQPixmap = QPixmap()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        file_name = e.mimeData().text()
        if file_name.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            e.acceptProposedAction()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        file_path = e.mimeData().text()
        file_path = re.sub('file:///', '', file_path)
        self._dropQPixmap = QPixmap(file_path)
        self.update()

    def clear(self) -> None:
        self.setText('\n\n Drop Image Here \n\n')
        self._dropQPixmap = QPixmap()
        self._resizeQPixmap = QPixmap()
        self._edgeQPixmap = QPixmap()

    def update(self) -> None:
        if self._dropQPixmap.height() > self._dropQPixmap.width():
            self._resizeQPixmap = self._dropQPixmap.scaledToHeight(170)
        else:
            self._resizeQPixmap = self._dropQPixmap.scaledToWidth(170)
        self.setPixmap(self._resizeQPixmap)

    @property
    def dropQPixmap(self):
        return self._dropQPixmap

    @dropQPixmap.setter
    def dropQPixmap(self, new_dropQPixmap):
        self._dropQPixmap = new_dropQPixmap

    @property
    def edgeQPixmap(self):
        return self._edgeQPixmap

    @edgeQPixmap.setter
    def edgeQPixmap(self, new_edgeQPixmap):
        self._edgeQPixmap = new_edgeQPixmap


class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.photoViewer = DLabel()
        mainLayout.addWidget(self.photoViewer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec_())