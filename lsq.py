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
        ax.scatter(csvData.iloc[:,[0]],csvData.iloc[:,[1]])
        window.setPlot()
        self.leastSquaresLine(self.convertToArray(csvData))
        

    def readFile(self, file):
        csvData = pd.read_csv(file)
        return csvData
    
    def convertToArray(self, csvData):
        array = csvData.to_numpy()
        print(array)
        return array
    
    def leastSquaresLine(self, array):
            array = np.c_[np.ones(array.shape[0]), array]
            A = array[:, [0,1]]
            b = array[:, [2]]

            aTrA = np.linalg.inv(np.matmul(np.transpose(A), A))
            aTrb = np.matmul(np.transpose(A), b)

            lineParams = np.matmul(aTrA, aTrb)
            global ax 
            ax.axline((0,lineParams[0][0]), slope=lineParams[1][0])


        
        
        


window = MainWindow()
sys.exit(app.exec())

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

#plt.show()

# Make work for more than 2 dimensional datasets