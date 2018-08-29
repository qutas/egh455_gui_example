#!/usr/bin/env python3

from PyQt5 import QtWidgets
from FILENAME import Ui_MainWindow
import sys

# The class that handles the application itself
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		# Create the Qt5 application backend
		super(ApplicationWindow, self).__init__()

		# Load in and display the UI
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

# The "main()" function, like a C program
def main():
	print("Loading application...")
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()
	print("Application loaded.")
	application.show()
	sys.exit(app.exec_())

# Provides a start point for out code
if __name__ == "__main__":
	main()
