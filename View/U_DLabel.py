from PyQt5.QtCore import Qt


class Ui_DLabel(object):
    def setupUi(self, Label):
        # QWidget --------------------------------------
        Label.setAcceptDrops(True)
        Label.setAlignment(Qt.AlignCenter)
        Label.setText('\n\n Drop Image Here \n\n')
