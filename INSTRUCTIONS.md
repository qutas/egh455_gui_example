## Installing PyQt5

PyQt5 is the default pyqt package for Python 3.6, and can be installed using Anoconda:
```sh
conda install pyqt
```

## Preparing the Application
The proccess below utilises the files `gui_template.py` and `example_window.ui`, which are both found in this repository. Before going further however, the `.ui` file must first be converted to a Python class (while it is not strictly necessary, it makes life a lot easier). To convert a `.ui` file to a Python class file, run the following command, replacing `FILENAME` with where appropriate (for the example, replace `FILENAME` with `example_window`):
```
python -m PyQt5.uic.pyuic -x FILENAME.ui -o FILENAME.py
```

#### Using the Python GUI Class
First, copy the code snippet below to be your program, and name the new file something like `application.py`, making sure that the Python GUI class that was created earlier exists in the same folder:
```py
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
```

Note that you will have to change `FILENAME` in the second line (`from FILENAME import Ui_MainWindow`) to match the filename used when you ran the `.ui` to `.py` conversion eariler.

At this point, you should be able to run your script and see your GUI displayed. When you exit the application, your script should also exit (and return to the command line):
```sh
python application.py
```

As a reference, a full template copy of this example is available in the repository as `gui_template.py`.

To import and use the GUI class (`FILENAME.py`), which defines the class `Ui_MainWindow`, first we have created a custom class `ApplicationWindow` that extends the class `PyQt5.QtWidgets.QMainWindow` (which provides the Qt5 application backend):
```py
# The class that handles the application itself
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		# Create the Qt5 application backend
		super(ApplicationWindow, self).__init__()
```


Once the application is created, the UI (`Ui_MainWindow`) can then be loaded and shown:
```py
# Load in and display the UI
self.ui = Ui_MainWindow()
self.ui.setupUi(self)
```

The rest of the template handles the actual loading of the application in a standard python way (by creating `main()` which loads in the custom class `ApplicationWindow` and stops the script from exiting.

## Adding Application Functionallity
With the application started and displayed, the next step is to add some functionallity to the widgets on your application.

In the `ApplicationWindow` class, create 4 new callbacks, one for each button (you can reuse a callback for multiple button presses, but we will keep it simple for now). Each function must recieve `self` as an argument (allowing it to use class variables), but can be used to do anything you wish:
```
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		...

	def callback_button_1(self):
		print("Button 1 pressed!")

	def callback_button_2(self):
		print("Button 2 pressed!")

	def callback_button_3(self):
		print("Button 3 pressed!")

	def callback_button_4(self):
		print("Button 4 pressed!")
```

Next, in `__init__(self)` of `ApplicationWindow`, connecting the button 'clicked' event to the appropriate functions will allow for that function to be run each time the button is pressed:
```
class ApplicationWindow(QtWidgets.QMainWindow):
	def __init__(self):
		# Create the Qt5 application backend
		...
		self.ui.setupUi(self)

		# Connect events (like button presses) to functions
		self.ui.button_1.clicked.connect(self.callback_button_1)
		self.ui.button_2.clicked.connect(self.callback_button_2)
		self.ui.button_3.clicked.connect(self.callback_button_3)
		self.ui.button_4.clicked.connect(self.callback_button_4)
```

Running the application again, you should now see messages printing to the terminal when you press a button.

#### Designing a custom GUI

TODO: Using Qt5 Designer
