import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd 
from PyQt5 import QtWidgets
import sys 

app = QtWidgets.QApplication(sys.argv)
dataset = None
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
        self.setMenus()
        self.setActions()
        self.connectActions()

    
    def setMenus(self):
        self.fileMenu = self.addMenu("File")
        self.fitMenu = self.addMenu("Fit")

    def setActions(self):
        self.actOpen = self.fileMenu.addAction("Open")
        self.actRandom = self.fileMenu.addAction("Randomise")

        self.actLinear = self.fitMenu.addAction("Linear")
        self.actLog = self.fitMenu.addAction("Logarithmic")

    def connectActions(self):
        self.actRandom.triggered.connect(self.randomiseData)
        self.actOpen.triggered.connect(self.fileOpen)
        self.actLinear.triggered.connect(self.linLine)
        self.actLog.triggered.connect(self.logLine)

    def fileOpen(self):
        global ax
        global dataset
        ax.clear()
        self.fileName, self.fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", ""
            , "Comma separated values (*.csv);;Excel File (*.xlsx *.xls)")
            # Add excel file functionality
        print(self.fileName)
        csvData = self.readFile(self.fileName)
        dataset = self.convertToArray(csvData)
        ax.scatter(csvData.iloc[:,[0]],csvData.iloc[:,[1]])
        window.setPlot()
        
    def randomiseData(self):
        global ax
        global dataset
        ax.clear()
        yVals = np.random.randint(-50, 50, size = 10)
        xVals = [-1,2,3,4,5,6,7,8,9,10]
        dataset = np.c_[np.array(np.transpose(xVals)), np.transpose(yVals)]
        ax.scatter(xVals,yVals)
        window.setPlot()
        

    def readFile(self, file):
        csvData = pd.read_csv(file)
        return csvData
    
    def convertToArray(self, csvData):
        array = csvData.to_numpy()
        print(array)
        return array
    
    def linLine(self): # y = ax + b
        global dataset
        global ax 
        if (dataset.__class__ == np.ndarray):
            xlim_original = ax.get_xlim()
            ylim_original = ax.get_ylim()

            array = np.c_[np.ones(dataset.shape[0]), dataset]
            A = array[:, [0,1]]
            b = array[:, [2]]

            aTrA = np.linalg.inv(np.matmul(np.transpose(A), A))
            aTrb = np.matmul(np.transpose(A), b)

            lineParams = np.matmul(aTrA, aTrb)
            ax.axline((0,lineParams[0][0]), slope=lineParams[1][0])
            ax.set_title(f"y = {lineParams[1,0]}x + {lineParams[0,0]}")

            ax.set_xlim(xlim_original)
            ax.set_ylim(ylim_original)
            window.setPlot()

    def logLine(self): # y = alnx + b
        global dataset
        global ax
        if (dataset.__class__ == np.ndarray):
            xlim_original = ax.get_xlim()
            ylim_original = ax.get_ylim()

            A = dataset[:, [0]]
            for ele in A:
                if ele <= 0:
                    print("Aborted: element of domain <= 0")
                    return
            A = np.c_[np.ones(dataset.shape[0]),np.log(A)]
            b = dataset[:, [1]]

            aTrA = np.linalg.inv(np.matmul(np.transpose(A), A))
            aTrb = np.matmul(np.transpose(A), b)
            lineParams = np.matmul(aTrA, aTrb) #[[b],[a]]
            f = lambda x,a,b: a * np.log(x) + b

            xVals = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1])
            yVals = f(xVals,lineParams[1,0],lineParams[0,0])
            ax.plot(xVals,yVals)
            ax.set_title(f"y = {lineParams[1,0]}lnx + {lineParams[0,0]}")

            ax.set_xlim(xlim_original)
            ax.set_ylim(ylim_original)
            window.setPlot()

window = MainWindow()
sys.exit(app.exec())