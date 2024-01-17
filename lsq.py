import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib as mpl 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 

FILE = None

app = QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self): 
        super(MainWindow, self).__init__()
        self.setWindowTitle("Least-Squares calculator")
        self.setGeometry(50, 50, 500, 300)
        self.show()
        self.initialplot()

    def initialplot(self):
        fig, ax = plt.subplots()
        self.setCentralWidget(FigureCanvas(fig))

    def fileSelector(self):
        btn = QtWidgets.QPushButton("Select file", self)
        


window = MainWindow()

#helloMsg = QtWidgets.QLabel("<h1>Hello, World!</h1>")
#mainLayout.addWidget(helloMsg)
sys.exit(app.exec())

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

#plt.show()