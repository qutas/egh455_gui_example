#!/usr/bin/env python3

from PyQt5 import QtWidgets
from example_window_video import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtMultimedia

# The class that handles the application itself
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		# Handle the application display
		super(ApplicationWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Connect events (like button presses) to functions
		self.ui.button_play.clicked.connect(self.callback_play)
		self.ui.button_pause.clicked.connect(self.callback_pause)
		self.ui.button_stop.clicked.connect(self.callback_stop)

		# Configure the video widget
		self.video_player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)

		# Load in a file to play
		file = QtCore.QDir.current().filePath("video.mp4")
		self.video_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file)))
		self.video_player.setVideoOutput(self.ui.video_widget)

	def callback_play(self):
		# Start video playback
		self.video_player.play()

	def callback_pause(self):
		# Pause video playback
		self.video_player.pause()

	def callback_stop(self):
		# Pause video playback
		self.video_player.stop()

# The "main()" function, like a C program
def main():
	print("Loading applicaiton...")
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()
	print("Application loaded.")
	application.show()
	sys.exit(app.exec_())

# Provides a start point for out code
if __name__ == "__main__":
	main()
