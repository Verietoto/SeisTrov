from PyQt5 import QtCore, QtGui, QtWidgets


class DashBoard(object):
    def setupUi_DashBoard(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 572)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.966507, y1:0.255, x2:0.971292, y2:1, stop:0.282297 rgba(0, 22, 40, 255), stop:1 rgba(21, 45, 91, 255));\n"
"border-width: 50px;\n"
"border-color: black;")
        self.mainPage = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy)
        self.mainPage.setAutoFillBackground(False)
        self.mainPage.setStyleSheet("")
        self.mainPage.setObjectName("mainPage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainPage)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideBarFrame = QtWidgets.QFrame(self.mainPage)
        self.sideBarFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.sideBarFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sideBarFrame.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.966507, y1:0.136, x2:0.971292, y2:1, stop:0.0861244 rgba(0, 0, 11, 173), stop:1 rgba(21, 45, 91, 255));\n"
"\n"
"border: None;\n"
"}")
        self.sideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBarFrame.setObjectName("sideBarFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideBarFrame)
        self.verticalLayout.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperSideBar = QtWidgets.QFrame(self.sideBarFrame)
        self.upperSideBar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.upperSideBar.setStyleSheet("background-color: none;\n"
"border-color: green;\n"
"")
        self.upperSideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upperSideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upperSideBar.setObjectName("upperSideBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.upperSideBar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toggleBTN = QtWidgets.QPushButton(self.upperSideBar)
        self.toggleBTN.setMinimumSize(QtCore.QSize(20, 20))
        self.toggleBTN.setMaximumSize(QtCore.QSize(50, 30))
        self.toggleBTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggleBTN.setStyleSheet("border: None;\n"
"color: None;\n"
"background-color: None;\n"
"selection-background-color: blue;;")
        self.toggleBTN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SideBar_Image/Menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleBTN.setIcon(icon)
        self.toggleBTN.setObjectName("toggleBTN")
        self.verticalLayout_3.addWidget(self.toggleBTN, 0, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(1, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.dashboardText = QtWidgets.QLabel(self.upperSideBar)
        self.dashboardText.setEnabled(True)
        self.dashboardText.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.dashboardText.setFont(font)
        self.dashboardText.setStyleSheet("background-color: None;\n"
"color: rgb(204, 204, 204)")
        self.dashboardText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dashboardText.setMidLineWidth(-2)
        self.dashboardText.setAlignment(QtCore.Qt.AlignCenter)
        self.dashboardText.setObjectName("dashboardText")
        self.verticalLayout_3.addWidget(self.dashboardText)
        self.dashboardText_2 = QtWidgets.QLabel(self.upperSideBar)
        self.dashboardText_2.setEnabled(True)
        self.dashboardText_2.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dashboardText_2.setFont(font)
        self.dashboardText_2.setStyleSheet("background-color: None;\n"
"color: rgb(204, 204, 204)")
        self.dashboardText_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dashboardText_2.setMidLineWidth(-2)
        self.dashboardText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dashboardText_2.setObjectName("dashboardText_2")
        self.verticalLayout_3.addWidget(self.dashboardText_2)
        self.mainTeks = QtWidgets.QLabel(self.upperSideBar)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.mainTeks.setFont(font)
        self.mainTeks.setStyleSheet("background-color: None;\n"
"color:rgb(90, 90, 90)")
        self.mainTeks.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTeks.setObjectName("mainTeks")
        self.verticalLayout_3.addWidget(self.mainTeks, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.upperSideBar)
        self.lowerSideBar = QtWidgets.QFrame(self.sideBarFrame)
        self.lowerSideBar.setStyleSheet("border: none;\n"
"background-color: none;\n"
"\n"
"")
        self.lowerSideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lowerSideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lowerSideBar.setObjectName("lowerSideBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lowerSideBar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.seismicViewerBTN = QtWidgets.QPushButton(self.lowerSideBar)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.seismicViewerBTN.setFont(font)
        self.seismicViewerBTN.setStyleSheet("QPushButton{\n"
"background-color: None;\n"
"color: rgb(208, 208, 208);}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(85, 255, 127);\n"
"color: black;}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("SideBar_Image/g5728.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seismicViewerBTN.setIcon(icon1)
        self.seismicViewerBTN.setIconSize(QtCore.QSize(40, 20))
        self.seismicViewerBTN.setObjectName("seismicViewerBTN")
        self.verticalLayout_2.addWidget(self.seismicViewerBTN)
        self.faultPredictionBTN = QtWidgets.QPushButton(self.lowerSideBar)
        self.faultPredictionBTN.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.faultPredictionBTN.setFont(font)
        self.faultPredictionBTN.setStyleSheet("QPushButton{\n"
"background-color: None;\n"
"color: rgb(208, 208, 208);}\n"
"\n"
"QPushButton::hover{\n"
"background-color: blue;}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("SideBar_Image/Fault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.faultPredictionBTN.setIcon(icon2)
        self.faultPredictionBTN.setIconSize(QtCore.QSize(25, 60))
        self.faultPredictionBTN.setObjectName("faultPredictionBTN")
        self.verticalLayout_2.addWidget(self.faultPredictionBTN)
        self.aboutSoftwareBTN = QtWidgets.QPushButton(self.lowerSideBar)
        self.aboutSoftwareBTN.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.aboutSoftwareBTN.setFont(font)
        self.aboutSoftwareBTN.setStyleSheet("QPushButton{\n"
"background-color: None;\n"
"color: rgb(208, 208, 208);}\n"
"\n"
"QPushButton::hover{\n"
"background-color: red;}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("SideBar_Image/About.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutSoftwareBTN.setIcon(icon3)
        self.aboutSoftwareBTN.setIconSize(QtCore.QSize(25, 50))
        self.aboutSoftwareBTN.setObjectName("aboutSoftwareBTN")
        self.verticalLayout_2.addWidget(self.aboutSoftwareBTN)
        self.contactMeBTN = QtWidgets.QPushButton(self.lowerSideBar)
        self.contactMeBTN.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.contactMeBTN.setFont(font)
        self.contactMeBTN.setStyleSheet("QPushButton{\n"
"background-color: None;\n"
"color: rgb(208, 208, 208);}\n"
"\n"
"QPushButton::hover{\n"
"background-color: yellow;\n"
"color: blue;}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("SideBar_Image/Contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contactMeBTN.setIcon(icon4)
        self.contactMeBTN.setIconSize(QtCore.QSize(30, 60))
        self.contactMeBTN.setObjectName("contactMeBTN")
        self.verticalLayout_2.addWidget(self.contactMeBTN)
        self.verticalLayout.addWidget(self.lowerSideBar)
        self.horizontalLayout.addWidget(self.sideBarFrame)
        self.contentFrame = QtWidgets.QFrame(self.mainPage)
        self.contentFrame.setStyleSheet("QFrame{\n"
"border:none\n"
"\n"
"\n"
"}")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.contentFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.contentFrame)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.seismicViewerPage = QtWidgets.QWidget()
        self.seismicViewerPage.setObjectName("seismicViewerPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.seismicViewerPage)
        self.verticalLayout_4.setContentsMargins(3, 0, 5, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.seismicViewerTop = QtWidgets.QFrame(self.seismicViewerPage)
        self.seismicViewerTop.setMaximumSize(QtCore.QSize(16777215, 60))
        self.seismicViewerTop.setStyleSheet("QFrame{\n"
"background-color: none;\n"
"color: white\n"
"\n"
"}")
        self.seismicViewerTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seismicViewerTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seismicViewerTop.setObjectName("seismicViewerTop")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.seismicViewerTop)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSeismicBTN = QtWidgets.QPushButton(self.seismicViewerTop)
        self.addSeismicBTN.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addSeismicBTN.setFont(font)
        self.addSeismicBTN.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("SideBar_Image/add_data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addSeismicBTN.setIcon(icon5)
        self.addSeismicBTN.setObjectName("addSeismicBTN")
        self.horizontalLayout_2.addWidget(self.addSeismicBTN, 0, QtCore.Qt.AlignBottom)
        self.colorMapBTN = QtWidgets.QComboBox(self.seismicViewerTop)
        self.colorMapBTN.setMaximumSize(QtCore.QSize(100, 23))
        self.colorMapBTN.setStyleSheet("QComboBox{\n"
"    color: Black;\n"
"    background-color: white;\n"
"\n"
"}")
        self.colorMapBTN.setObjectName("colorMapBTN")
        self.colorMapBTN.addItem("")
        self.colorMapBTN.addItem("")
        self.colorMapBTN.addItem("")
        self.horizontalLayout_2.addWidget(self.colorMapBTN, 0, QtCore.Qt.AlignBottom)
        self.Widged = QtWidgets.QLabel(self.seismicViewerTop)
        self.Widged.setStyleSheet("background-color:None;\n"
"color:rgb(255, 255, 255, 100)")
        self.Widged.setAlignment(QtCore.Qt.AlignCenter)
        self.Widged.setObjectName("Widged")
        self.horizontalLayout_2.addWidget(self.Widged, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.seismicViewerTop)
        self.seismicViewerScreen = QtWidgets.QFrame(self.seismicViewerPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seismicViewerScreen.sizePolicy().hasHeightForWidth())
        self.seismicViewerScreen.setSizePolicy(sizePolicy)
        self.seismicViewerScreen.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.seismicViewerScreen.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}")
        self.seismicViewerScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seismicViewerScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seismicViewerScreen.setObjectName("seismicViewerScreen")
        self.verticalLayout_4.addWidget(self.seismicViewerScreen)
        self.seismicViewerBot = QtWidgets.QFrame(self.seismicViewerPage)
        self.seismicViewerBot.setMaximumSize(QtCore.QSize(900, 90))
        self.seismicViewerBot.setStyleSheet("QFrame{\n"
"background-color: none;\n"
"color: white\n"
"\n"
"}")
        self.seismicViewerBot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seismicViewerBot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seismicViewerBot.setObjectName("seismicViewerBot")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.seismicViewerBot)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.viewText = QtWidgets.QLabel(self.seismicViewerBot)
        self.viewText.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.viewText.setStyleSheet("color: white;\n"
"background-color: None;")
        self.viewText.setAlignment(QtCore.Qt.AlignCenter)
        self.viewText.setObjectName("viewText")
        self.verticalLayout_5.addWidget(self.viewText)
        self.twoDBTN = QtWidgets.QRadioButton(self.seismicViewerBot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoDBTN.sizePolicy().hasHeightForWidth())
        self.twoDBTN.setSizePolicy(sizePolicy)
        self.twoDBTN.setMaximumSize(QtCore.QSize(50, 16777215))
        self.twoDBTN.setStyleSheet("QRadioButton {\n"
"    background-color:       None;\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       Green;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       White;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"")
        self.twoDBTN.setObjectName("twoDBTN")
        self.verticalLayout_5.addWidget(self.twoDBTN)
        self.threeDBTN = QtWidgets.QRadioButton(self.seismicViewerBot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeDBTN.sizePolicy().hasHeightForWidth())
        self.threeDBTN.setSizePolicy(sizePolicy)
        self.threeDBTN.setMaximumSize(QtCore.QSize(50, 16777215))
        self.threeDBTN.setStyleSheet("QRadioButton {\n"
"    background-color:       None;\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       Green;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       White;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"")
        self.threeDBTN.setObjectName("threeDBTN")
        self.verticalLayout_5.addWidget(self.threeDBTN)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(13)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tSliceNumber_2 = QtWidgets.QLineEdit(self.seismicViewerBot)
        self.tSliceNumber_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tSliceNumber_2.sizePolicy().hasHeightForWidth())
        self.tSliceNumber_2.setSizePolicy(sizePolicy)
        self.tSliceNumber_2.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(8)
        self.tSliceNumber_2.setFont(font)
        self.tSliceNumber_2.setStyleSheet("QLineEdit {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: white;\n"
"        color: black\n"
"  }\n"
"\n"
"QLineEdit::disabled {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: Grey;;\n"
"      color: dark Grey;\n"
"  }\n"
"\n"
"")
        self.tSliceNumber_2.setObjectName("tSliceNumber_2")
        self.gridLayout_2.addWidget(self.tSliceNumber_2, 1, 6, 1, 1)
        self.addTsliceBTN_2 = QtWidgets.QPushButton(self.seismicViewerBot)
        self.addTsliceBTN_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTsliceBTN_2.sizePolicy().hasHeightForWidth())
        self.addTsliceBTN_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addTsliceBTN_2.setFont(font)
        self.addTsliceBTN_2.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("SideBar_Image/addBTNS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTsliceBTN_2.setIcon(icon6)
        self.addTsliceBTN_2.setIconSize(QtCore.QSize(17, 32))
        self.addTsliceBTN_2.setObjectName("addTsliceBTN_2")
        self.gridLayout_2.addWidget(self.addTsliceBTN_2, 0, 6, 1, 1)
        self.typeBTN_2 = QtWidgets.QComboBox(self.seismicViewerBot)
        self.typeBTN_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeBTN_2.sizePolicy().hasHeightForWidth())
        self.typeBTN_2.setSizePolicy(sizePolicy)
        self.typeBTN_2.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Loma")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.typeBTN_2.setFont(font)
        self.typeBTN_2.setStyleSheet("QComboBox{\n"
"    color: Black;\n"
"    background-color: White;\n"
"\n"
"}\n"
"QComboBox::disabled{\n"
"    color: Black;\n"
"    background-color:Grey;\n"
"\n"
"}")
        self.typeBTN_2.setObjectName("typeBTN_2")
        self.typeBTN_2.addItem("")
        self.typeBTN_2.addItem("")
        self.typeBTN_2.addItem("")
        self.gridLayout_2.addWidget(self.typeBTN_2, 0, 0, 1, 1)
        self.addXlnesliceBTN_3 = QtWidgets.QPushButton(self.seismicViewerBot)
        self.addXlnesliceBTN_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addXlnesliceBTN_3.sizePolicy().hasHeightForWidth())
        self.addXlnesliceBTN_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addXlnesliceBTN_3.setFont(font)
        self.addXlnesliceBTN_3.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.addXlnesliceBTN_3.setIcon(icon6)
        self.addXlnesliceBTN_3.setIconSize(QtCore.QSize(17, 32))
        self.addXlnesliceBTN_3.setObjectName("addXlnesliceBTN_3")
        self.gridLayout_2.addWidget(self.addXlnesliceBTN_3, 0, 4, 1, 1)
        self.xlineSliceNumber_3 = QtWidgets.QLineEdit(self.seismicViewerBot)
        self.xlineSliceNumber_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xlineSliceNumber_3.sizePolicy().hasHeightForWidth())
        self.xlineSliceNumber_3.setSizePolicy(sizePolicy)
        self.xlineSliceNumber_3.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(8)
        self.xlineSliceNumber_3.setFont(font)
        self.xlineSliceNumber_3.setStyleSheet("QLineEdit {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: white;\n"
"        color: black\n"
"  }\n"
"\n"
"QLineEdit::disabled {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: Grey;;\n"
"      color: dark Grey;\n"
"  }\n"
"\n"
"")
        self.xlineSliceNumber_3.setObjectName("xlineSliceNumber_3")
        self.gridLayout_2.addWidget(self.xlineSliceNumber_3, 1, 4, 1, 1)
        self.twoDNumber_2 = QtWidgets.QLineEdit(self.seismicViewerBot)
        self.twoDNumber_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoDNumber_2.sizePolicy().hasHeightForWidth())
        self.twoDNumber_2.setSizePolicy(sizePolicy)
        self.twoDNumber_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(8)
        self.twoDNumber_2.setFont(font)
        self.twoDNumber_2.setStyleSheet("QLineEdit {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: white;\n"
"        color: black\n"
"  }\n"
"\n"
"QLineEdit::disabled {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: Grey;;\n"
"      color: dark Grey;\n"
"  }\n"
"\n"
"")
        self.twoDNumber_2.setObjectName("twoDNumber_2")
        self.gridLayout_2.addWidget(self.twoDNumber_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.addInlineBTN_2 = QtWidgets.QPushButton(self.seismicViewerBot)
        self.addInlineBTN_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addInlineBTN_2.sizePolicy().hasHeightForWidth())
        self.addInlineBTN_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addInlineBTN_2.setFont(font)
        self.addInlineBTN_2.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.addInlineBTN_2.setIcon(icon6)
        self.addInlineBTN_2.setIconSize(QtCore.QSize(17, 32))
        self.addInlineBTN_2.setObjectName("addInlineBTN_2")
        self.gridLayout_2.addWidget(self.addInlineBTN_2, 0, 2, 1, 1)
        self.inlineNumber_2 = QtWidgets.QLineEdit(self.seismicViewerBot)
        self.inlineNumber_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inlineNumber_2.sizePolicy().hasHeightForWidth())
        self.inlineNumber_2.setSizePolicy(sizePolicy)
        self.inlineNumber_2.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(8)
        self.inlineNumber_2.setFont(font)
        self.inlineNumber_2.setStyleSheet("QLineEdit {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: white;\n"
"        color: black\n"
"  }\n"
"\n"
"QLineEdit::disabled {\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      background: Grey;;\n"
"      color: dark Grey;\n"
"  }\n"
"\n"
"")
        self.inlineNumber_2.setObjectName("inlineNumber_2")
        self.gridLayout_2.addWidget(self.inlineNumber_2, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 5, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addWidget(self.seismicViewerBot)
        self.seismicViewerTop.raise_()
        self.seismicViewerScreen.raise_()
        self.addTsliceBTN_2.raise_()
        self.seismicViewerBot.raise_()
        self.stackedWidget.addWidget(self.seismicViewerPage)
        self.faultPredictPage = QtWidgets.QWidget()
        self.faultPredictPage.setObjectName("faultPredictPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.faultPredictPage)
        self.verticalLayout_6.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.faultPredictTop = QtWidgets.QFrame(self.faultPredictPage)
        self.faultPredictTop.setMaximumSize(QtCore.QSize(16777215, 60))
        self.faultPredictTop.setStyleSheet("QFrame{\n"
"background-color: none;\n"
"color: white\n"
"\n"
"}")
        self.faultPredictTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faultPredictTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faultPredictTop.setObjectName("faultPredictTop")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.faultPredictTop)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.changeAxisBTN = QtWidgets.QPushButton(self.faultPredictTop)
        self.changeAxisBTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.changeAxisBTN.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("SideBar_Image/swipe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeAxisBTN.setIcon(icon7)
        self.changeAxisBTN.setIconSize(QtCore.QSize(70, 100))
        self.changeAxisBTN.setObjectName("changeAxisBTN")
        self.horizontalLayout_4.addWidget(self.changeAxisBTN)
        self.whatIsThis = QtWidgets.QPushButton(self.faultPredictTop)
        self.whatIsThis.setMaximumSize(QtCore.QSize(40, 16777215))
        self.whatIsThis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.whatIsThis.setStyleSheet("background-color: None;\n"
";border: None;\n"
"color: white;\n"
"QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.whatIsThis.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("SideBar_Image/ask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.whatIsThis.setIcon(icon8)
        self.whatIsThis.setIconSize(QtCore.QSize(25, 100))
        self.whatIsThis.setObjectName("whatIsThis")
        self.horizontalLayout_4.addWidget(self.whatIsThis)
        self.addCNNBTN = QtWidgets.QPushButton(self.faultPredictTop)
        self.addCNNBTN.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addCNNBTN.setFont(font)
        self.addCNNBTN.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.addCNNBTN.setIcon(icon5)
        self.addCNNBTN.setObjectName("addCNNBTN")
        self.horizontalLayout_4.addWidget(self.addCNNBTN)
        self.addSeismicBTN2 = QtWidgets.QPushButton(self.faultPredictTop)
        self.addSeismicBTN2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(9)
        self.addSeismicBTN2.setFont(font)
        self.addSeismicBTN2.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.addSeismicBTN2.setIcon(icon5)
        self.addSeismicBTN2.setObjectName("addSeismicBTN2")
        self.horizontalLayout_4.addWidget(self.addSeismicBTN2)
        self.Widged_2 = QtWidgets.QLabel(self.faultPredictTop)
        self.Widged_2.setStyleSheet("background-color:None;\n"
"color:rgb(255, 255, 255, 100)")
        self.Widged_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Widged_2.setObjectName("Widged_2")
        self.horizontalLayout_4.addWidget(self.Widged_2)
        self.verticalLayout_6.addWidget(self.faultPredictTop)
        self.faultPredictScreen = QtWidgets.QFrame(self.faultPredictPage)
        self.faultPredictScreen.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.faultPredictScreen.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}")
        self.faultPredictScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faultPredictScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faultPredictScreen.setObjectName("faultPredictScreen")
        self.verticalLayout_6.addWidget(self.faultPredictScreen)
        self.faultPredictBot = QtWidgets.QFrame(self.faultPredictPage)
        self.faultPredictBot.setMaximumSize(QtCore.QSize(16777215, 80))
        self.faultPredictBot.setStyleSheet("QFrame{\n"
"background-color: none;\n"
"color: white\n"
"\n"
"}")
        self.faultPredictBot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faultPredictBot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faultPredictBot.setObjectName("faultPredictBot")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.faultPredictBot)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.enchantingText = QtWidgets.QLabel(self.faultPredictBot)
        self.enchantingText.setStyleSheet("color: rgb(103, 103, 103);\n"
"background-color: None;")
        self.enchantingText.setAlignment(QtCore.Qt.AlignCenter)
        self.enchantingText.setObjectName("enchantingText")
        self.verticalLayout_7.addWidget(self.enchantingText)
        self.clipBTN = QtWidgets.QCheckBox(self.faultPredictBot)
        self.clipBTN.setStyleSheet("QCheckBox {\n"
"    background-color:       None;\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       Green;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       White;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"")
        self.clipBTN.setObjectName("clipBTN")
        self.verticalLayout_7.addWidget(self.clipBTN)
        self.gaussianBlurBTN = QtWidgets.QCheckBox(self.faultPredictBot)
        self.gaussianBlurBTN.setStyleSheet("QCheckBox {\n"
"    background-color:       None;\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       Green;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       White;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"")
        self.gaussianBlurBTN.setObjectName("gaussianBlurBTN")
        self.verticalLayout_7.addWidget(self.gaussianBlurBTN)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.predictFault = QtWidgets.QPushButton(self.faultPredictBot)
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(12)
        self.predictFault.setFont(font)
        self.predictFault.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        self.predictFault.setIcon(icon5)
        self.predictFault.setObjectName("predictFault")
        self.verticalLayout_8.addWidget(self.predictFault, 0, QtCore.Qt.AlignLeft)
        self.predictFault_2 = QtWidgets.QPushButton(self.faultPredictBot)
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(12)
        self.predictFault_2.setFont(font)
        self.predictFault_2.setStyleSheet("QPushButton{\n"
"    color: White;\n"
"    background-color: None;\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: orange;    \n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("SideBar_Image/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.predictFault_2.setIcon(icon9)
        self.predictFault_2.setObjectName("predictFault_2")
        self.verticalLayout_8.addWidget(self.predictFault_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addWidget(self.faultPredictBot)
        self.stackedWidget.addWidget(self.faultPredictPage)
        self.aboutSoftwarePage = QtWidgets.QWidget()
        self.aboutSoftwarePage.setObjectName("aboutSoftwarePage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.aboutSoftwarePage)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.geInTouvhTXT_2 = QtWidgets.QLabel(self.aboutSoftwarePage)
        self.geInTouvhTXT_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setItalic(True)
        self.geInTouvhTXT_2.setFont(font)
        self.geInTouvhTXT_2.setStyleSheet("border: None;\n"
"background-color: None;\n"
"color: rgb(116, 103, 255);")
        self.geInTouvhTXT_2.setObjectName("geInTouvhTXT_2")
        self.verticalLayout_9.addWidget(self.geInTouvhTXT_2)
        self.label = QtWidgets.QLabel(self.aboutSoftwarePage)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.aboutSoftwarePage)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser_2.setStyleSheet("border: None;\n"
"color: White;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_9.addWidget(self.textBrowser_2)
        self.label_2 = QtWidgets.QLabel(self.aboutSoftwarePage)
        self.label_2.setMaximumSize(QtCore.QSize(500, 500))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Background/myPhoto.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.aboutSoftwarePage)
        self.contactMePage = QtWidgets.QWidget()
        self.contactMePage.setObjectName("contactMePage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.contactMePage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.geInTouvhTXT = QtWidgets.QLabel(self.contactMePage)
        self.geInTouvhTXT.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(12)
        font.setItalic(True)
        self.geInTouvhTXT.setFont(font)
        self.geInTouvhTXT.setStyleSheet("border: None;\n"
"background-color: None;\n"
"color: rgb(116, 103, 255);")
        self.geInTouvhTXT.setObjectName("geInTouvhTXT")
        self.verticalLayout_10.addWidget(self.geInTouvhTXT)
        self.textBrowser = QtWidgets.QTextBrowser(self.contactMePage)
        self.textBrowser.setStyleSheet("border: None;\n"
"color: white;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_10.addWidget(self.textBrowser)
        self.stackedWidget.addWidget(self.contactMePage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.contentFrame)
        MainWindow.setCentralWidget(self.mainPage)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboardText.setText(_translate("MainWindow", "<strong>SEIS</strong>TROV"))
        self.dashboardText_2.setText(_translate("MainWindow", "BETA"))
        self.mainTeks.setText(_translate("MainWindow", "MAIN"))
        self.seismicViewerBTN.setText(_translate("MainWindow", " Seismic Viewer"))
        self.faultPredictionBTN.setText(_translate("MainWindow", " Fault Predict"))
        self.aboutSoftwareBTN.setText(_translate("MainWindow", " About Software"))
        self.contactMeBTN.setText(_translate("MainWindow", " Contact Me"))
        self.addSeismicBTN.setText(_translate("MainWindow", "Add Seismic"))
        self.colorMapBTN.setItemText(0, _translate("MainWindow", "Greys"))
        self.colorMapBTN.setItemText(1, _translate("MainWindow", "seismic"))
        self.colorMapBTN.setItemText(2, _translate("MainWindow", "RdYlBu"))
        self.Widged.setText(_translate("MainWindow", "No Seismic Inputed"))
        self.viewText.setText(_translate("MainWindow", "View"))
        self.twoDBTN.setText(_translate("MainWindow", "2D"))
        self.threeDBTN.setText(_translate("MainWindow", "3D"))
        self.tSliceNumber_2.setText(_translate("MainWindow", "Time Number"))
        self.addTsliceBTN_2.setText(_translate("MainWindow", "Add Tslice to 3D"))
        self.typeBTN_2.setItemText(0, _translate("MainWindow", "Inline"))
        self.typeBTN_2.setItemText(1, _translate("MainWindow", "Crossline"))
        self.typeBTN_2.setItemText(2, _translate("MainWindow", "TimeSlice"))
        self.addXlnesliceBTN_3.setText(_translate("MainWindow", "Add Xline to 3D"))
        self.xlineSliceNumber_3.setText(_translate("MainWindow", "Xline Number"))
        self.twoDNumber_2.setText(_translate("MainWindow", "Type Number"))
        self.addInlineBTN_2.setText(_translate("MainWindow", "Add Inline to 3D"))
        self.inlineNumber_2.setText(_translate("MainWindow", "Inline Number"))
        self.changeAxisBTN.setText(_translate("MainWindow", "Change Axis"))
        self.addCNNBTN.setText(_translate("MainWindow", "Add CNN Model"))
        self.addSeismicBTN2.setText(_translate("MainWindow", "Add Seismic"))
        self.Widged_2.setText(_translate("MainWindow", "No Seismic Inputed"))
        self.enchantingText.setText(_translate("MainWindow", "Enchating"))
        self.clipBTN.setText(_translate("MainWindow", "Clip"))
        self.gaussianBlurBTN.setText(_translate("MainWindow", "Gaussian Blur"))
        self.predictFault.setText(_translate("MainWindow", "PREDICT FAULT"))
        self.predictFault_2.setText(_translate("MainWindow", "SAVE PREDICTION"))
        self.geInTouvhTXT_2.setText(_translate("MainWindow", "<html><head/><body><p>About Software</p><p><br/></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">This UI software is my very first GUI i made using python code. Plotting seismic using PyVista libraries and predicting fault on seismic section using Deep Leaning concept. Convolutional Neural Networks is apllied as main predictor in this software. of course this algorithm still have many flaw, any suggestion and comment of you guys are needed. Feel free to contact me in &quot;Contact me&quot; section.</span></p></body></html>"))
        self.geInTouvhTXT.setText(_translate("MainWindow", "<strong> Get In Touch </strong> With Me\n"
""))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Feel Free to Contact me via Linkedin or Whatsapp:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Linkedin: www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Whatsapp: +6289686646839</p></body></html>"))

