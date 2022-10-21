"""
My Camera Application
outhor : Sa'ad

"""

import sys

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import *


class Window(QWidget) :
    # My Camera Application

    def __init__(self) :
        super().__init__() 

        # variables for app window
        self.window_width = 640
        self.window_height = 400

        # image variables
        self.img_width = 640
        self.img_height = 400

        # setup the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        self.camera_icon = QIcon(cap_icon_path)

        # setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self) :
        # contains all UI things
        # layout
        grid = QGridLayout()
        self.setLayout(grid)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.img_width, self.img_height)

        # capture btn
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 30; border : 2px solid black; border-width : 3px")
        self.capture_btn.setFixedSize(50, 50)
        self.capture_btn.clicked.connect(self.save_image)

        if not self.timer.isActive() :
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        grid.addWidget(self.capture_btn, 0, 0)
        grid.addWidget(self.image_label, 0 , 1)
        
        self.show()

    def update(self) :
        # update frames
        _, self.frame = self.cap.read()
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_image(self) :
        # save image from camera
        print("saving image")
        cv2.imwrite("my_img.jpg", self.frame)

    def record(self) :
        # record video
        pass


cap_icon_path = "assets/icons/capture.png"

# run 
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
