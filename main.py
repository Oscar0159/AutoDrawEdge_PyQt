import sys

from PyQt5 import QtWidgets

from Controller.C_MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()

    with open('Qstyle.qss', 'r') as f:
        window.setStyleSheet(f.read())

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
