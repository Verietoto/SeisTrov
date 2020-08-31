# Some Libraries
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
import os
import segyio
import pyvistaqt as pv
import pyvista as pv2

import matplotlib
matplotlib.rcParams['figure.figsize'] = [10, 10] # for square canvas
matplotlib.rcParams['figure.subplot.left'] = 0
matplotlib.rcParams['figure.subplot.bottom'] = 0
matplotlib.rcParams['figure.subplot.right'] = 1
matplotlib.rcParams['figure.subplot.top'] = 1
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PyQt5.QtCore import *
import numpy as np
from LoadingScreen import Ui_loadingWindow
from DashBoard import DashBoard

# Some Variables
COUNTER = 0
pages = {"button": ["aboutSoftwareBTN", "currentButton"],
         "styleSheet": [
             "QPushButton{background-color: None; color:white; QPushButton::hover{background-color:yellow;}}",
             "QPushButton{background-color: red; color:white; QPushButton::hover{background-color:orange;}}"]}
TOGGLE = 1
seismicText = ['NO SEISMIC INPUTED']

class MplCanvas(FigureCanvas):

    def __init__(self):
        fig = Figure(figsize=(1,1), dpi=10, facecolor="Black")
        self.axes = fig.add_subplot()
        self.axes.set_facecolor="Black"
        super(MplCanvas, self).__init__(fig)


class openFileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.main = QMainWindow()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.main.setWindowTitle(self.title)
        self.main.setGeometry(self.left, self.top, self.width, self.height)
        self.main.move(300,300)

        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Seismic Data", "",
                                                  "SEGY (*.segy);;SGY (*.sgy);;Numpy (*.npy)", options=options)

        # global seismicText
        global seismicText

        seismicText[0] = fileName
        self.readSeismic()


    def readSeismic(self):
        global seismic

        if seismicText[0].endswith("segy") or seismicText[0].endswith("sgy"):
            try:
                x = segyio.open(seismicText[0])
                seismic = np.empty((len(x.ilines), len(x.xlines), len(x.samples)))
                tr = 0
                for i in range(len(x.ilines)):
                    for j in range(len(x.xlines)):
                        seismic[i, j, :] = x.trace[tr]
                        tr += 1
            except ValueError:
                with segyio.open(seismicText[0], "r",ignore_geometry=True) as segyfile:
                    seismic = segyfile.trace.raw[:]
        else:
            seismic = np.load(seismicText[0])

# dashBoard Class
class openDashBoard():
    def __init__(self):
        self.mainWindow = QMainWindow()
        self.dashBoard = DashBoard()
        self.dashBoard.setupUi_DashBoard(self.mainWindow)
        # self.openSeismic = openFileDialog()

        # Connect Stacked Widged + Change Color
        pages["button"][1] = self.dashBoard.aboutSoftwareBTN
        pages["styleSheet"][0] = self.dashBoard.aboutSoftwareBTN.styleSheet()
        self.dashBoard.aboutSoftwareBTN.setStyleSheet(pages["styleSheet"][1])

        self.dashBoard.seismicViewerBTN.clicked.connect(
            lambda: self.changePage(self.dashBoard.seismicViewerPage, self.dashBoard.seismicViewerBTN))
        self.dashBoard.faultPredictionBTN.clicked.connect(
            lambda: self.changePage(self.dashBoard.faultPredictPage, self.dashBoard.faultPredictionBTN))
        self.dashBoard.aboutSoftwareBTN.clicked.connect(
            lambda: self.changePage(self.dashBoard.aboutSoftwarePage, self.dashBoard.aboutSoftwareBTN))
        self.dashBoard.contactMeBTN.clicked.connect(
            lambda: self.changePage(self.dashBoard.contactMePage, self.dashBoard.contactMeBTN))

        # Side Bar Toggle Hide and Show
        self.dashBoard.toggleBTN.clicked.connect(self.toggleBarConnect)

        ## Seismic Viewer Page

        #   add Seismic Button and change Text of No Seismic Inputed
        self.dashBoard.addSeismicBTN.clicked.connect(self.addData)

        # Setting Widged for 2D and 3D
        self.dashBoard.twoDBTN.clicked.connect(lambda: self.showWidged(self.dashBoard.twoDBTN))
        self.dashBoard.threeDBTN.clicked.connect(lambda: self.showWidged(self.dashBoard.threeDBTN))

        # Plotting 2D
        self.seismicViewerLayOut = QtWidgets.QVBoxLayout(self.dashBoard.seismicViewerScreen)
        self.seismicViewerLayOut.setContentsMargins(0, 0, 0, 0)
        self.dashBoard.twoDBTN.clicked.connect(self.addMatplotlib)
        self.dashBoard.twoDNumber_2.returnPressed.connect(self.plot2D)

        #Plotting 3D
        self.dashBoard.threeDBTN.clicked.connect(self.addPyVista)
        self.dashBoard.addInlineBTN_2.clicked.connect(lambda: self.plot3D(self.dashBoard.addInlineBTN_2))
        self.dashBoard.addXlnesliceBTN_3.clicked.connect(lambda: self.plot3D(self.dashBoard.addXlnesliceBTN_3))
        self.dashBoard.addTsliceBTN_2.clicked.connect(lambda: self.plot3D(self.dashBoard.addTsliceBTN_2))

    def plot3D(self, button):
        if button == self.dashBoard.addInlineBTN_2:
            position = int(self.dashBoard.inlineNumber_2.text())
            self.plotCanvas3D.add_mesh(self.grid.slice(normal="X", origin=(position, 0, 0)),
                                       clim=[-self.v, self.v], cmap=self.dashBoard.colorMapBTN.currentText())

        elif button == self.dashBoard.addXlnesliceBTN_3:
            position = int(self.dashBoard.xlineSliceNumber_3.text())
            self.plotCanvas3D.add_mesh(self.grid.slice(normal="Y", origin=(0,position,0)),
                                       clim=[-self.v, self.v], cmap=self.dashBoard.colorMapBTN.currentText())

        elif button == self.dashBoard.addTsliceBTN_2:
            position = int(self.dashBoard.tSliceNumber_2.text())
            self.plotCanvas3D.add_mesh(self.grid.slice(normal="Z", origin=(0,0,position)),
                                       clim=[-self.v, self.v], cmap=self.dashBoard.colorMapBTN.currentText())

    def plot2D(self):
        if self.dashBoard.typeBTN_2.currentIndex() == 0:
            seismic2DPlot = self.dashBoard.twoDNumber_2.text()
            seismic2DPlot = seismic[int(seismic2DPlot),:,:]
            v = np.percentile(seismic2DPlot,99)

        elif self.dashBoard.typeBTN_2.currentIndex() == 1:
            seismic2DPlot = self.dashBoard.twoDNumber_2.text()
            seismic2DPlot = seismic[:,int(seismic2DPlot), :]
            v = np.percentile(seismic2DPlot, 99)
        elif self.dashBoard.typeBTN_2.currentIndex() == 2:
            seismic2DPlot = self.dashBoard.twoDNumber_2.text()
            seismic2DPlot = seismic[:,:, int(seismic2DPlot)]
            v = np.percentile(seismic2DPlot, 99)
        self.plotSeismic2D(seismic2DPlot, v)

    def plotSeismic2D(self, data, v):
        self.plotCanvas.axes.clear()
        self.plotCanvas.axes.imshow(data.T, vmin=-v, vmax=v, cmap=self.dashBoard.colorMapBTN.currentText(), aspect='auto')
        self.plotCanvas.draw()


    def addMatplotlib(self):
        self.plotCanvas = MplCanvas()
        for i in reversed(range(self.seismicViewerLayOut.count())):
            self.seismicViewerLayOut.itemAt(i).widget().setParent(None)
        self.seismicViewerLayOut.addWidget(self.plotCanvas)

    def addPyVista(self):
        self.plotCanvas3D = pv.QtInteractor(self.dashBoard.seismicViewerScreen)
        self.v = np.percentile(seismic,99)
        self.grid = pv2.UniformGrid()
        self.grid.origin = (0,0,0)
        self.grid.dimensions = seismic.shape
        self.grid.point_arrays["Ampplitude"] = seismic.flatten(order="F")
        for i in reversed(range(self.seismicViewerLayOut.count())):
            self.seismicViewerLayOut.itemAt(i).widget().setParent(None)
        self.seismicViewerLayOut.addWidget(self.plotCanvas3D)







    def showWidged(self, btn):
        if btn == (self.dashBoard.twoDBTN):
            self.dashBoard.typeBTN_2.setEnabled(True)
            self.dashBoard.twoDNumber_2.setEnabled(True)
            self.dashBoard.addInlineBTN_2.setEnabled(False)
            self.dashBoard.addXlnesliceBTN_3.setEnabled(False)
            self.dashBoard.addTsliceBTN_2.setEnabled(False)
            self.dashBoard.inlineNumber_2.setEnabled(False)
            self.dashBoard.xlineSliceNumber_3.setEnabled(False)
            self.dashBoard.tSliceNumber_2.setEnabled(False)


        elif btn == self.dashBoard.threeDBTN:
            self.dashBoard.addInlineBTN_2.setEnabled(True)
            self.dashBoard.addXlnesliceBTN_3.setEnabled(True)
            self.dashBoard.addTsliceBTN_2.setEnabled(True)
            self.dashBoard.inlineNumber_2.setEnabled(True)
            self.dashBoard.xlineSliceNumber_3.setEnabled(True)
            self.dashBoard.tSliceNumber_2.setEnabled(True)
            self.dashBoard.typeBTN_2.setEnabled(False)
            self.dashBoard.twoDNumber_2.setEnabled(False)



    def addData(self):
        self.openDialog = openFileDialog()
        self.dashBoard.Widged.setText(os.path.basename(seismicText[0]))

    def changePage(self, page, btn):
        self.dashBoard.stackedWidget.setCurrentWidget(page)
        self.updateColor(btn)


    def updateColor(self, btn):
        pages["button"][0] = pages["button"][1]
        (pages["button"][0].setStyleSheet(pages["styleSheet"][0]))
        pages["styleSheet"][0] = btn.styleSheet()
        pages["button"][1] = btn
        (pages["button"][1].setStyleSheet(pages["styleSheet"][1]))


    def toggleBarConnect(self):
        global TOGGLE
        TOGGLE *= -1
        if TOGGLE == -1:
            self.dashBoard.sideBarFrame.setMaximumSize(QtCore.QSize(20, 10000))
        else:
            self.dashBoard.sideBarFrame.setMaximumSize(QtCore.QSize(200, 10000))


# Main Window
class homePage():
    def __init__(self):
        # Making Main Window
        self.mainWindow = QMainWindow()

        # Embedded Main Window to Loading Screen and move to center of screen
        self.loadingScreen = Ui_loadingWindow()
        self.loadingScreen.setupUi(self.mainWindow)
        self.mainWindow.move(300, 100)

        # Set Window into Frameless Window and show Window
        self.mainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.mainWindow.show()

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)

        # Editing Loading Text
        QtCore.QTimer.singleShot(4500,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>WELCOME</strong> TO SEISTROV"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(2000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> DATA BASED"))

    def progress(self):
        global COUNTER

        self.loadingScreen.progressBar.setValue(COUNTER)
        COUNTER += 1

        if COUNTER > 100:
            self.timer.stop()
            self.mainWindow.close()
            self.dashBoard = openDashBoard()
            self.dashBoard.mainWindow.showMaximized()


# Main Function
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = homePage()
    sys.exit(app.exec_())