from PyQt5.QtCore import QPointF, QRect, QSize, QMetaObject, Qt
from PyQt5.QtGui import QColor, QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QPushButton, QWidget, QLabel, QSlider

from MyWidget.W_DLabel import DLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # QMainWindow ----------------------------------------------------------------------------
        MainWindow.resize(600, 350)
        MainWindow.setWindowTitle('AutoDraw')
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowIcon(QIcon('images/AutoDrawEdge.ico'))

        # QWidget ----------------------------------------------------------------------------
        # After widget just for adding shadow
        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        MainWindow.setCentralWidget(self.centralwidget)

        # panel widget
        # panel label for adding shadow to this widget
        self.lab_panelshadowAfter = QLabel(self.centralwidget)
        self.lab_panelshadowAfter.setGeometry(QRect(275, 5, 310, 340))
        self.lab_panelshadowAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=36, offset=QPointF(-10, -10),
                                                                     color=QColor('#62D5FF')))
        self.lab_panelshadow = QLabel(self.centralwidget)
        self.lab_panelshadow.setGeometry(QRect(275, 5, 310, 340))
        self.lab_panelshadow.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=36, offset=QPointF(10, 10),
                                                                color=QColor('#489DCF')))
        self.panelwidget = QWidget(self.centralwidget)
        self.panelwidget.setObjectName('panelwidget')
        self.panelwidget.setGeometry(QRect(275, 5, 310, 340))

        # QSlider ----------------------------------------------------------------------------
        # line weight slider
        self.sli_line = QSlider(self.panelwidget)
        self.sli_line.setObjectName("sli_line")
        self.sli_line.setRange(1, 10)
        self.sli_line.setPageStep(1)
        self.sli_line.setGeometry(QRect(95, 8, 165, 32))
        self.sli_line.setOrientation(Qt.Horizontal)
        self.sli_line.setTickPosition(QSlider.TicksBothSides)

        # denoise level slider
        self.sli_denoise = QSlider(self.panelwidget)
        self.sli_denoise.setObjectName("sli_denoise")
        self.sli_denoise.setRange(1, 10)
        self.sli_denoise.setPageStep(1)
        self.sli_denoise.setGeometry(QRect(95, 43, 165, 32))
        self.sli_denoise.setOrientation(Qt.Horizontal)
        self.sli_denoise.setTickPosition(QSlider.TicksBothSides)

        # blur index slider
        self.sli_blur = QSlider(self.panelwidget)
        self.sli_blur.setObjectName("sli_blur")
        self.sli_blur.setRange(0, 9)
        self.sli_blur.setPageStep(1)
        self.sli_blur.setGeometry(QRect(95, 78, 165, 32))
        self.sli_blur.setOrientation(Qt.Horizontal)
        self.sli_blur.setTickPosition(QSlider.TicksBothSides)

        # click event send speed slider
        self.sli_click = QSlider(self.panelwidget)
        self.sli_click.setObjectName("sli_click")
        self.sli_click.setRange(1, 10)
        self.sli_click.setPageStep(1)
        self.sli_click.setGeometry(QRect(95, 113, 165, 32))
        self.sli_click.setOrientation(Qt.Horizontal)
        self.sli_click.setTickPosition(QSlider.TicksBothSides)

        # DLabel ----------------------------------------------------------------------------
        # After dlabel just for adding shadow
        self.dlabelAfter = DLabel(self.centralwidget)
        self.dlabelAfter.setGeometry(QRect(40, 85, 180, 180))
        self.dlabelAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=36, offset=QPointF(-10, -10),
                                                                       color=QColor('#62D5FF')))
        self.dlabel = DLabel(self.centralwidget)
        self.dlabel.setGeometry(QRect(40, 85, 180, 180))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dlabel.setFont(font)
        self.dlabel.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=36, offset=QPointF(10, 10),
                                                                       color=QColor('#489DCF')))

        # QLabel ----------------------------------------------------------------------------
        # line weight label
        self.lab_line = QLabel(self.panelwidget)
        self.lab_line.setObjectName("lab_line")
        self.lab_line.setText('線條粗細')
        self.lab_line.setGeometry(QRect(20, 15, 70, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_line.setFont(font)

        # line weight number label
        self.lab_lineNum = QLabel(self.panelwidget)
        self.lab_lineNum.setObjectName("lab_lineNum")
        self.lab_lineNum.setText(str(self.sli_line.value()))
        self.lab_lineNum.setAlignment(Qt.AlignCenter)
        self.lab_lineNum.setGeometry(QRect(270, 15, 20, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_lineNum.setFont(font)

        # denoise level label
        self.lab_denoise = QLabel(self.panelwidget)
        self.lab_denoise.setObjectName("lab_denoise")
        self.lab_denoise.setText('降噪等級')
        self.lab_denoise.setGeometry(QRect(20, 50, 70, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_denoise.setFont(font)

        # denoise level number label
        self.lab_denoiseNum = QLabel(self.panelwidget)
        self.lab_denoiseNum.setObjectName("lab_denoiseNum")
        self.lab_denoiseNum.setText(str(self.sli_denoise.value()))
        self.lab_denoiseNum.setAlignment(Qt.AlignCenter)
        self.lab_denoiseNum.setGeometry(QRect(270, 50, 20, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_denoiseNum.setFont(font)

        # blur index label
        self.lab_blur = QLabel(self.panelwidget)
        self.lab_blur.setObjectName("lab_blur")
        self.lab_blur.setText('模糊程度')
        self.lab_blur.setGeometry(QRect(20, 85, 70, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_blur.setFont(font)

        # blur index number label
        self.lab_blurNum = QLabel(self.panelwidget)
        self.lab_blurNum.setObjectName("lab_blurNum")
        self.lab_blurNum.setText(str(self.sli_blur.value()))
        self.lab_blurNum.setAlignment(Qt.AlignCenter)
        self.lab_blurNum.setGeometry(QRect(270, 85, 20, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_blurNum.setFont(font)

        # click event send speed label
        self.lab_click = QLabel(self.panelwidget)
        self.lab_click.setObjectName("lab_click")
        self.lab_click.setText('點擊速率')
        self.lab_click.setGeometry(QRect(20, 120, 70, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_click.setFont(font)

        # click event send speed number label
        self.lab_clickNum = QLabel(self.panelwidget)
        self.lab_clickNum.setObjectName("lab_clickNum")
        self.lab_clickNum.setText(str(self.sli_click.value()))
        self.lab_clickNum.setAlignment(Qt.AlignCenter)
        self.lab_clickNum.setGeometry(QRect(270, 120, 20, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_clickNum.setFont(font)

        # QPushButton --------------------------------------
        # After button just for adding shadow
        # menu button
        self.btn_menuAfter = QPushButton(self.centralwidget)
        self.btn_menuAfter.setObjectName('btn_menuAfter')
        self.btn_menuAfter.setGeometry(QRect(5, 5, 25, 25))
        self.btn_menuAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(-3, -3),
                                                                       color=QColor('#62D5FF')))
        self.btn_menu = QPushButton(self.centralwidget)
        self.btn_menu.setObjectName('btn_menu')
        self.btn_menu.setGeometry(QRect(5, 5, 25, 25))
        self.btn_menu.setIcon(QIcon(QPixmap('images/menu.png')))
        self.btn_menu.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(3, 3),
                                                                       color=QColor('#489DCF')))

        # stickie button
        self.btn_stickieAfter = QPushButton(self.centralwidget)
        self.btn_stickieAfter.setObjectName('btn_stickieAfter')
        self.btn_stickieAfter.setGeometry(QRect(230, 10, 25, 25))
        self.btn_stickieAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(-3, -3),
                                                                       color=QColor('#62D5FF')))
        self.btn_stickie = QPushButton(self.centralwidget)
        self.btn_stickie.setObjectName('btn_stickie')
        self.btn_stickie.setGeometry(QRect(230, 10, 25, 25))
        self.btn_stickie.setIcon(QIcon(QPixmap('images/stickie.png')))
        self.btn_stickie.setCheckable(True)
        self.btn_stickie.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(3, 3),
                                                                       color=QColor('#489DCF')))

        # information button
        self.btn_infoAfter = QPushButton(self.centralwidget)
        self.btn_infoAfter.setObjectName('btn_infoAfter')
        self.btn_infoAfter.setGeometry(QRect(5, 320, 25, 25))
        self.btn_infoAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(-3, -3),
                                                                       color=QColor('#62D5FF')))
        self.btn_info = QPushButton(self.centralwidget)
        self.btn_info.setObjectName('btn_info')
        self.btn_info.setGeometry(QRect(5, 320, 25, 25))
        self.btn_info.setIcon(QIcon(QPixmap('images/information.png')))
        self.btn_info.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(3, 3),
                                                                       color=QColor('#489DCF')))

        # theme button
        self.btn_themeAfter = QPushButton(self.centralwidget)
        self.btn_themeAfter.setObjectName('btn_themeAfter')
        self.btn_themeAfter.setGeometry(QRect(230, 320, 25, 25))
        self.btn_themeAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(-3, -3),
                                                                       color=QColor('#62D5FF')))
        self.btn_theme = QPushButton(self.centralwidget)
        self.btn_theme.setObjectName('btn_theme')
        self.btn_theme.setGeometry(QRect(230, 320, 25, 25))
        self.btn_theme.setIcon(QIcon(QPixmap('images/moon.png')))
        self.btn_theme.setCheckable(True)
        self.btn_theme.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, offset=QPointF(3, 3),
                                                                       color=QColor('#489DCF')))

        # screenshot button
        self.btn_screenshotAfter = QPushButton(self.centralwidget)
        self.btn_screenshotAfter.setObjectName('btn_screenshotAfter')
        self.btn_screenshotAfter.setGeometry(QRect(40, 20, 40, 40))
        self.btn_screenshotAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                       color=QColor('#62D5FF')))
        self.btn_screenshot = QPushButton(self.centralwidget)
        self.btn_screenshot.setObjectName('btn_screenshot')
        self.btn_screenshot.setGeometry(QRect(40, 20, 40, 40))
        self.btn_screenshot.setIcon(QIcon(QPixmap('images/screenshot.png')))
        self.btn_screenshot.setIconSize(QSize(25, 25))
        self.btn_screenshot.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                  color=QColor('#489DCF')))

        # file button
        self.btn_fileAfter = QPushButton(self.centralwidget)
        self.btn_fileAfter.setObjectName('btn_fileAfter')
        self.btn_fileAfter.setGeometry(QRect(110, 20, 40, 40))
        self.btn_fileAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                           color=QColor('#62D5FF')))
        self.btn_file = QPushButton(self.centralwidget)
        self.btn_file.setObjectName('btn_file')
        self.btn_file.setGeometry(QRect(110, 20, 40, 40))
        self.btn_file.setIcon(QIcon(QPixmap('images/folder.png')))
        self.btn_file.setIconSize(QSize(25, 25))
        self.btn_file.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                      color=QColor('#489DCF')))

        # url button
        self.btn_urlAfter = QPushButton(self.centralwidget)
        self.btn_urlAfter.setObjectName('btn_urlAfter')
        self.btn_urlAfter.setGeometry(QRect(180, 20, 40, 40))
        self.btn_urlAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                        color=QColor('#62D5FF')))
        self.btn_url = QPushButton(self.centralwidget)
        self.btn_url.setObjectName('btn_url')
        self.btn_url.setGeometry(QRect(180, 20, 40, 40))
        self.btn_url.setIcon(QIcon(QPixmap('images/url.png')))
        self.btn_url.setIconSize(QSize(25, 25))
        self.btn_url.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                   color=QColor('#489DCF')))

        # copy button
        self.btn_copyAfter = QPushButton(self.centralwidget)
        self.btn_copyAfter.setObjectName('btn_copyAfter')
        self.btn_copyAfter.setGeometry(QRect(40, 290, 40, 40))
        self.btn_copyAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                       color=QColor('#62D5FF')))
        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName('btn_copy')
        self.btn_copy.setGeometry(QRect(40, 290, 40, 40))
        self.btn_copy.setIcon(QIcon(QPixmap('images/copy.png')))
        self.btn_copy.setIconSize(QSize(25, 25))
        self.btn_copy.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                  color=QColor('#489DCF')))

        # download button
        self.btn_downloadAfter = QPushButton(self.centralwidget)
        self.btn_downloadAfter.setObjectName('btn_downloadAfter')
        self.btn_downloadAfter.setGeometry(QRect(110, 290, 40, 40))
        self.btn_downloadAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                       color=QColor('#62D5FF')))
        self.btn_download = QPushButton(self.centralwidget)
        self.btn_download.setObjectName('btn_download')
        self.btn_download.setGeometry(QRect(110, 290, 40, 40))
        self.btn_download.setIcon(QIcon(QPixmap('images/download.png')))
        self.btn_download.setIconSize(QSize(25, 25))
        self.btn_download.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                       color=QColor('#489DCF')))

        # trash button
        self.btn_trashAfter = QPushButton(self.centralwidget)
        self.btn_trashAfter.setObjectName('btn_downloadAfter')
        self.btn_trashAfter.setGeometry(QRect(180, 290, 40, 40))
        self.btn_trashAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(-4, -4),
                                                                           color=QColor('#62D5FF')))
        self.btn_trash = QPushButton(self.centralwidget)
        self.btn_trash.setObjectName('btn_trash')
        self.btn_trash.setGeometry(QRect(180, 290, 40, 40))
        self.btn_trash.setIcon(QIcon(QPixmap('images/trash.png')))
        self.btn_trash.setIconSize(QSize(25, 25))
        self.btn_trash.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=8, offset=QPointF(4, 4),
                                                                      color=QColor('#489DCF')))

        # draw button
        self.btn_drawAfter = QPushButton(self.panelwidget)
        self.btn_drawAfter.setObjectName('btn_drawAfter')
        self.btn_drawAfter.setGeometry(QRect(20, 285, 270, 40))
        self.btn_drawAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=24, offset=QPointF(-8, -8),
                                                                        color=QColor('#62D5FF')))
        self.btn_draw = QPushButton(self.panelwidget)
        self.btn_draw.setObjectName('btn_draw')
        self.btn_draw.setGeometry(QRect(20, 285, 270, 40))
        self.btn_draw.setIcon(QIcon(QPixmap('images/draw.png')))
        self.btn_draw.setIconSize(QSize(25, 25))
        self.btn_draw.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=24, offset=QPointF(8, 8),
                                                                   color=QColor('#489DCF')))

        # monitor button
        self.btn_monitorAfter = QPushButton(self.panelwidget)
        self.btn_monitorAfter.setObjectName('btn_monitorAfter')
        self.btn_monitorAfter.setGeometry(QRect(20, 150, 270, 120))
        self.btn_monitorAfter.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=24, offset=QPointF(-8, -8),
                                                                       color=QColor('#62D5FF')))
        self.btn_monitor = QPushButton(self.panelwidget)
        self.btn_monitor.setObjectName('btn_monitor')
        self.btn_monitor.setGeometry(QRect(20, 150, 270, 120))
        self.btn_monitor.setIcon(QIcon(QPixmap('images/monitor.png')))
        self.btn_monitor.setIconSize(QSize(50, 50))
        self.btn_monitor.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=24, offset=QPointF(8, 8),
                                                                  color=QColor('#489DCF')))



        QMetaObject.connectSlotsByName(MainWindow)