from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()#IMP!!!!!!!!!!!!!!!!

app.exec_()