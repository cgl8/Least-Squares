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
        self.setFixedSize(500, 300)
        self.show()
        self.initialplot()
        menu = MenuBar()
        self.setMenuBar(menu)

    def initialplot(self):
        fig, ax = plt.subplots()
        self.setCentralWidget(FigureCanvas(fig))

class MenuBar(QtWidgets.QMenuBar):

    def __init__(self):
        super(MenuBar, self).__init__()
        self.fileMenu = self.addMenu("File")
        self.actOpen = self.fileMenu.addAction("Open")
        self.actOpen.triggered.connect(self.fileOpen)

    def fileOpen(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "Comma separated values (*.csv);;Excel File (*.xlsx *.xls)")
        
        


window = MainWindow()
sys.exit(app.exec())

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

#plt.show()

# Make work for more than 2 dimensional datasets