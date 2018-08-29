#!/usr/bin/env python3

from PyQt5 import QtWidgets
from example_window import Ui_MainWindow
import sys

# The class that handles the application itself
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		# Handle the application display
		super(ApplicationWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Connect events (like button presses) to functions
		self.ui.button_1.clicked.connect(self.callback_button_1)
		self.ui.button_2.clicked.connect(self.callback_button_2)
		self.ui.button_3.clicked.connect(self.callback_button_3)
		self.ui.button_4.clicked.connect(self.callback_button_4)

	def callback_button_1(self):
		print("Button 1 pressed!")

	def callback_button_2(self):
		print("Button 2 pressed!")

	def callback_button_3(self):
		print("Button 3 pressed!")

	def callback_button_4(self):
		print("Button 4 pressed!")

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
