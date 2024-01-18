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
        self.actRandom = self.fileMenu.addAction("Randomise")
        self.actRandom.triggered.connect(self.randomiseData)
        self.actOpen.triggered.connect(self.fileOpen)

    def fileOpen(self):
        global ax
        ax.clear()
        self.fileName, self.fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", ""
            , "Comma separated values (*.csv);;Excel File (*.xlsx *.xls)")
            # Add excel file functionality?
        print(self.fileName)
        csvData = self.readFile(self.fileName)
        ax.scatter(csvData.iloc[:,[0]],csvData.iloc[:,[1]])
        window.setPlot()
        self.leastSquaresLine(self.convertToArray(csvData))
        
    def randomiseData(self):
        global ax
        ax.clear()
        yVals = np.random.randint(-50, 50, size = 10)
        xVals = [-1,0,1,2,3,4,5,6,7,8]
        dataset = np.c_[np.array(np.transpose(xVals)), np.transpose(yVals)]
        ax.scatter(xVals,yVals)
        self.leastSquaresLine(dataset)
        window.setPlot()
        

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

# Make work for more than 2 dimensional datasets