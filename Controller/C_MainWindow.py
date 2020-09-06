from PyQt5.QtCore import pyqtSlot, QPointF, QRect, Qt, QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QFileDialog, QApplication, QStyleOptionSlider, \
    QToolTip, QInputDialog, QLineEdit

from Controller.C_CaptureWindow import CaptureWidget
from Controller.C_SettingWindow import SettingWindow
from Controller.C_InformationWindow import InformationWindow
from Controller.C_UrlWindow import UrlWindow
from Model.M_AutoDraw import AutoDrawManager
from Model.M_ScreenInfo import ScreenInfoManager
from View.U_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.style = QApplication.style()
        self.opt = QStyleOptionSlider()

        self.settingwindow = SettingWindow()
        self.infowindow = InformationWindow()
        self.urlwindow = UrlWindow()
        self.urlwindow.editFibisgedSignal.connect(self.get_url)
        self.capturewidget = CaptureWidget()
        self.ui.dlabel.dropSignal.connect(self.set_dropImg)

        self.adManager = AutoDrawManager()
        self.scManager = ScreenInfoManager()

    def closeEvent(self, e) -> None:
        QApplication.closeAllWindows()

    @pyqtSlot()
    def on_btn_menu_clicked(self):
        self.settingwindow.show()

    @pyqtSlot()
    def on_btn_stickie_clicked(self):
        if self.ui.btn_stickie.isChecked():
            self.ui.btn_stickie.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,'
                                              'stop:0 #489DCF, stop:1 #62D5FF);')
            self.ui.btn_stickie.setGraphicsEffect(None)
            self.ui.btn_stickieAfter.setGraphicsEffect(None)
        else:
            self.ui.btn_stickie.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,'
                                              'stop:0 #5BC6FF, stop:1 #4DA7DB);')
            self.ui.btn_stickie.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(3, 3),
                                                                            color=QColor('#489DCF')))
            self.ui.btn_stickieAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(-3, -3),
                                                                                 color=QColor('#62D5FF')))

    @pyqtSlot()
    def on_btn_info_clicked(self):
        self.infowindow.show()

    @pyqtSlot()
    def on_btn_theme_clicked(self):
        if self.ui.btn_theme.isChecked():
            self.ui.btn_theme.setIcon(QIcon(QPixmap('images/sun.png')))
        else:
            self.ui.btn_theme.setIcon(QIcon(QPixmap('images/moon.png')))

    @pyqtSlot()
    def on_btn_screenshot_clicked(self):
        self.capturewidget.show()
        # for setting capture region and image after capture the screen
        self.capturewidget.captureSignal.connect(self.set_capture)

    @pyqtSlot()
    def on_btn_file_clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "選取圖檔", '.', "Image File (*.png *.jpg)")
        if filename != '':
            print(filename)
            self.adManager.file2Img(filename)

        self.ui.dlabel.dropQPixmap = QPixmap(filename)
        self.ui.dlabel.update()

    @pyqtSlot()
    def on_btn_url_clicked(self):
        self.urlwindow.show()
        self.urlwindow.setGeometry(self.x(), self.y()-self.urlwindow.height(),
                                   self.urlwindow.width(), self.urlwindow.height())

    @pyqtSlot()
    def on_btn_copy_clicked(self):
        if not self.ui.dlabel.dropQPixmap.isNull():
            clipboard = QApplication.clipboard()
            clipboard.setPixmap(self.ui.dlabel.dropQPixmap)

    @pyqtSlot()
    def on_btn_download_clicked(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "圖檔保存", '.', "PNG Files (*.png);;JPEG Files (*.jpg)")
        if save_path != '' and not self.ui.dlabel.dropQPixmap.isNull():
            self.ui.dlabel.dropQPixmap.save(save_path)

    @pyqtSlot()
    def on_btn_trash_clicked(self):
        self.ui.dlabel.clear()

    @pyqtSlot()
    def on_btn_draw_clicked(self):
        self.adManager.updateImg()
        self.adManager.draw(self.adManager.padEdgeImg)

    @pyqtSlot()
    def on_btn_monitor_clicked(self):
        self.capturewidget.show()
        # for setting draw region and image after capture the screen
        self.capturewidget.captureSignal.connect(self.set_draw)

    @pyqtSlot(int)
    def on_sli_line_valueChanged(self, value):
        self.adManager.lineWeight = value*2 + 1
        self.ui.sli_line.setToolTip(str(value))
        self.ui.lab_lineNum.setText(str(value))

    @pyqtSlot(int)
    def on_sli_denoise_valueChanged(self, value):
        self.adManager.denoiseLevel = value
        self.ui.sli_denoise.setToolTip(str(value))
        self.ui.lab_denoiseNum.setText(str(value))

    @pyqtSlot(int)
    def on_sli_blur_valueChanged(self, value):
        if value == 0:
            self.adManager.blurIndex = value
        else:
            self.adManager.blurIndex = value+1
        self.ui.sli_blur.setToolTip(str(value))
        self.ui.lab_blurNum.setText(str(value))

    @pyqtSlot(int)
    def on_sli_click_valueChanged(self, value):
        self.adManager.clickEvent = value*50
        self.ui.sli_click.setToolTip(str(value))
        self.ui.lab_clickNum.setText(str(value))

    def set_capture(self, rect: QRect):
        self.capturewidget.captureSignal.disconnect(self.set_capture)
        self.scManager.captureRegion = rect
        self.scManager.refreshScrInfo()
        self.scManager.screenshot()  # get new screen image
        qpixmap = self.scManager.get_captureRegionImg()
        self.adManager.qpixmap2Img(qpixmap)
        self.ui.dlabel.dropQPixmap = qpixmap
        self.ui.dlabel.update()

    def set_draw(self, rect: QRect):
        self.capturewidget.captureSignal.disconnect(self.set_draw)
        self.scManager.drawRegion = rect
        self.scManager.refreshScrInfo()
        self.scManager.screenshot()  # get new screen image
        self.adManager.drawRegion = rect
        drawReginImg = self.scManager.screenImg
        painter = QPainter(drawReginImg)
        penRectangle = QPen(Qt.red)
        penRectangle.setWidth(25)
        painter.setPen(penRectangle)
        painter.drawRect(rect)
        self.ui.btn_monitor.setIcon(QIcon(drawReginImg))
        self.ui.btn_monitor.setIconSize(QSize(self.ui.btn_monitor.width(), self.ui.btn_monitor.height()))

    def set_dropImg(self):
        self.adManager.qpixmap2Img(self.ui.dlabel.dropQPixmap)

    def get_url(self, url):
        self.adManager.url2Img(url)
        # self.adManager.getQPixmap(self.adManager.oriImg)
        self.ui.dlabel.dropQPixmap = self.adManager.getQPixmap(self.adManager.oriImg)
        self.ui.dlabel.update()
