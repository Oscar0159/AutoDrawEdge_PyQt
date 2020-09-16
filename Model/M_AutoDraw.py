import ctypes
import time

import cv2
import numpy as np
from PyQt5.QtCore import QUrl, QRect
from PyQt5.QtGui import QPixmap, qRed, qGreen, qBlue, qRgb, QImage
from PyQt5.QtWidgets import QApplication


def qtpixmap2cvimg(qpixmap):
    qimg = qpixmap.toImage()

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


def cvimg2qpixmap(cvimg):
    if cvimg.size != 0:
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        h, w, channel = cvimg.shape
        bytesPerLine = 3 * w
        qImg = QImage(cvimg.data, w, h, bytesPerLine, QImage.Format_RGB888)
        return QPixmap(qImg)


def cv_imread(filename):
    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    return img


def mouse_click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up


class AutoDrawManager:
    def __init__(self):
        self._lineWeight = 3  # 線條粗細
        self._denoiseLevel = 6  # 降噪等級
        self._blurIndex = 2  # 模糊係數
        self._drawRegion = QRect(0, 0, 1, 1)  # 繪製區域
        self._clickEvent = 200  # 每 1 秒傳送 N 個滑鼠點擊事件

        self._oriImg = np.zeros((0, 0, 3), np.uint8)  # 原始圖檔
        self._resizeImg = np.zeros((0, 0, 3), np.uint8)  # 以繪製區域大小調整過後的圖片(預覽用)
        self._oriEdgeImg = np.zeros((0, 0, 3), np.uint8)  # 黑邊圖, 原圖轉換過的黑邊圖(存檔用)
        self._padImg = np.zeros((0, 0, 3), np.uint8)
        self._padEdgeImg = np.zeros((0, 0, 3), np.uint8)   # 繪製圖, 超出圖片部分補白底大小等於繪製區域(繪製用)


    def getQPixmap(self, cvImg):
        if cvImg.size != 0:
            return cvimg2qpixmap(cvImg)
        else:
            return QPixmap()

    def showImg(self, cvImg):
        if cvImg.size != 0:
            cv2.imshow('img', cvImg)

    def isBlack(self, pixel):
        return pixel.tolist() == [0, 0, 0, 255]

    def draw(self, cvImg):
        if cvImg.size != 0:
            x1= self._drawRegion.x() + QApplication.desktop().x()
            y1 = self._drawRegion.y() + QApplication.desktop().y()
            print('開始繪製-->')
            img = cv2.cvtColor(cvImg, cv2.COLOR_BGR2BGRA)
            h, w = img.shape[0:2]
            count = 0
            for i in range(h):
                for j in range(w):
                    # 減少黑點數量
                    if i % 2 == 0 and j % 2 == 0:
                        if self.isBlack(img[i][j]):
                            count += 1
                            mouse_click(x1 + j, y1 + i)
                            if count == self._clickEvent:
                                count = 0
                                time.sleep(1)
            print('滑鼠點擊事件全數傳送完畢')
            print('如有繪製錯誤請降低傳送事件速率')
            print('------------------------------')

    def edge(self, cvImg):
        if cvImg.size != 0:
            if self._blurIndex != 0:
                cvImg = cv2.blur(cvImg, (self._blurIndex, self._blurIndex))
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
            img_edge = cv2.adaptiveThreshold(cvImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                             blockSize=self._lineWeight, C=self._denoiseLevel)
            return img_edge

    def resize(self, cvImg):
        if cvImg.size != 0 :
            regionW, regionH = self._drawRegion.width(), self._drawRegion.height()
            min_side = regionH if regionW > regionH else regionW
            h, w = cvImg.shape[0:2]

            scale = max(w, h) / float(min_side)
            new_w, new_h = int(w / scale), int(h / scale)
            new_w = 1 if new_w == 0 else new_w
            new_h = 1 if new_h == 0 else new_h
            return cv2.resize(cvImg, (new_w, new_h))

    def padding(self, cvImg):
        if cvImg.size != 0:
            regionW, regionH = self._drawRegion.width(), self._drawRegion.height()
            min_side = regionH if regionW > regionH else regionW
            h, w = cvImg.shape[0:2]

            scale = max(w, h) / float(min_side)
            new_w, new_h = int(w / scale), int(h / scale)
            new_w = 1 if new_w == 0 else new_w
            new_h = 1 if new_h == 0 else new_h

            if new_w % 2 != 0 and new_h % 2 == 0:
                top, bottom, left, right = int((regionH - new_h) / 2), int((regionH - new_h) / 2), \
                                           int((regionW - new_w) / 2 + 1), int((regionW - new_w) / 2)
            elif new_h % 2 != 0 and new_w % 2 == 0:
                top, bottom, left, right = int((regionH - new_h) / 2 + 1), int((regionH - new_h) / 2), \
                                           int((regionW - new_w) / 2), int((regionW - new_w) / 2)
            elif new_h % 2 == 0 and new_w % 2 == 0:
                top, bottom, left, right = int((regionH - new_h) / 2), int((regionH - new_h) / 2), \
                                           int((regionW - new_w) / 2), int((regionW - new_w) / 2)
            else:
                top, bottom, left, right = int((regionH - new_h) / 2 + 1), int((regionH - new_h) / 2), \
                                           int((regionW - new_w) / 2 + 1), int((regionW - new_w) / 2)

            return cv2.copyMakeBorder(cvImg, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    def updateImg(self):
        if self._oriImg.size != 0:
            self._resizeImg = self.resize(self._oriImg)
            self._oriEdgeImg = self.edge(self._oriImg)
            self._padImg = self.padding(self._resizeImg)
            self._padEdgeImg = self.edge(self._padImg)
        else:
            print('origin image is empty!')

    def url2Img(self, url):
        try:
            cap = cv2.VideoCapture(url)
            if (cap.isOpened()):
                _, self._oriImg = cap.read()
        except:
            print('url error')

    def file2Img(self, filename):
        self._oriImg = cv_imread(filename)

    def qpixmap2Img(self, qpixmap):
        self._oriImg = qtpixmap2cvimg(qpixmap)

    @property
    def lineWeight(self):
        return self._lineWeight

    @lineWeight.setter
    def lineWeight(self, new_lineWeight):
        self._lineWeight = new_lineWeight

    @property
    def denoiseLevel(self):
        return self._denoiseLevel

    @denoiseLevel.setter
    def denoiseLevel(self, new_denoiseLevel):
        self._denoiseLevel = new_denoiseLevel

    @property
    def blurIndex(self):
        return self._blurIndex

    @blurIndex.setter
    def blurIndex(self, new_blurIndex):
        self._blurIndex = new_blurIndex

    @property
    def drawRegion(self):
        return self._drawRegion

    @drawRegion.setter
    def drawRegion(self, new_drawRegion):
        self._drawRegion = new_drawRegion

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, new_sec):
        self._sec = new_sec

    @property
    def clickEvent(self):
        return self._clickEvent

    @clickEvent.setter
    def clickEvent(self, new_clickEvent):
        self._clickEvent = new_clickEvent

    @property
    def oriImg(self):
        return self._oriImg

    @property
    def resizeImg(self):
        return self._resizeImg

    @property
    def oriEdgeImg(self):
        return self._oriEdgeImg

    @property
    def padImg(self):
        return self._padImg

    @property
    def padEdgeImg(self):
        return self._padEdgeImg
