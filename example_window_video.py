# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example_window_video.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(70, 200, 80, 25))
        self.button_play.setObjectName("button_play")
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setGeometry(QtCore.QRect(170, 200, 80, 25))
        self.button_pause.setObjectName("button_pause")
        self.video_widget = QVideoWidget(self.centralwidget)
        self.video_widget.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.video_widget.setObjectName("video_widget")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(270, 200, 80, 25))
        self.button_stop.setObjectName("button_stop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_play.setText(_translate("MainWindow", "Play"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))

from PyQt5.QtMultimediaWidgets import QVideoWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

