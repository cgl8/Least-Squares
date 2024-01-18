import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib as mpl 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd 
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 

app = QtWidgets.QApplication(sys.argv)
fig, ax = plt.subplots() #Main figure and axes

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self): 
        super(MainWindow, self).__init__()
        self.setWindowTitle("Least-Squares calculator")
        self.setFixedSize(500, 300)
        self.show()
        self.setPlot()
        menu = MenuBar()
        self.setMenuBar(menu)

    def setPlot(self):
        self.setCentralWidget(FigureCanvas(fig))

class MenuBar(QtWidgets.QMenuBar):

    def __init__(self):
        super(MenuBar, self).__init__()
        self.fileMenu = self.addMenu("File")
        self.actOpen = self.fileMenu.addAction("Open")
        self.actOpen.triggered.connect(self.fileOpen)

    def fileOpen(self):
        self.fileName, self.fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", ""
            , "Comma separated values (*.csv);;Excel File (*.xlsx *.xls)")
        print(self.fileName)
        csvData = self.readFile(self.fileName)
        global ax
        ax.plot(csvData.iloc[:,[0]],csvData.iloc[:,[1]])
        window.setPlot()

    def readFile(self, file):
        csvData = pd.read_csv(file)
        return csvData
        

        
        
        


window = MainWindow()
sys.exit(app.exec())

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

#plt.show()

# Make work for more than 2 dimensional datasets