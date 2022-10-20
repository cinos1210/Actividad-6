from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
from scipy.optimize import linprog
import sys

app =QApplication()

window = MainWindow()

window.show()

sys.exit(app.exec_())
