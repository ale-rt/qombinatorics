# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QombGui.ui'
#
# Created: Mon May  5 22:16:15 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from random import randint
import random
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,334,369).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon("../messagebox_warning.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.output = QtGui.QTextBrowser(self.centralwidget)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(226,217,212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.output.setPalette(palette)
        self.output.setObjectName("output")
        self.vboxlayout.addWidget(self.output)

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")

        c = 4
        
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.vboxlayout2.addWidget(self.label_3)

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.vboxlayout2.addWidget(self.label_4)
        self.hboxlayout.addLayout(self.vboxlayout2)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.permutationSpin = QtGui.QSpinBox(self.tab)
        self.permutationSpin.setObjectName("permutationSpin")
        self.hboxlayout1.addWidget(self.permutationSpin)

        self.sliderSetPermutations = QtGui.QSlider(self.tab)
        self.sliderSetPermutations.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSetPermutations.setObjectName("sliderSetPermutations")
        self.hboxlayout1.addWidget(self.sliderSetPermutations)
        self.vboxlayout3.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.picksSpin = QtGui.QSpinBox(self.tab)
        self.picksSpin.setObjectName("picksSpin")
        self.hboxlayout2.addWidget(self.picksSpin)

        self.sliderPicks = QtGui.QSlider(self.tab)
        self.sliderPicks.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPicks.setObjectName("sliderPicks")
        self.hboxlayout2.addWidget(self.sliderPicks)
        self.vboxlayout3.addLayout(self.hboxlayout2)
        self.hboxlayout.addLayout(self.vboxlayout3)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.vboxlayout5.addWidget(self.label)

        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.vboxlayout5.addWidget(self.label_2)
        self.hboxlayout3.addLayout(self.vboxlayout5)

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.spinSet = QtGui.QSpinBox(self.tab_2)
        self.spinSet.setObjectName("spinSet")
        self.hboxlayout4.addWidget(self.spinSet)

        self.sliderSet = QtGui.QSlider(self.tab_2)
        self.sliderSet.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSet.setObjectName("sliderSet")
        self.hboxlayout4.addWidget(self.sliderSet)
        self.vboxlayout6.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.spinSubset = QtGui.QSpinBox(self.tab_2)
        self.spinSubset.setObjectName("spinSubset")
        self.hboxlayout5.addWidget(self.spinSubset)

        self.sliderSubset = QtGui.QSlider(self.tab_2)
        self.sliderSubset.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSubset.setObjectName("sliderSubset")
        self.hboxlayout5.addWidget(self.sliderSubset)
        self.vboxlayout6.addLayout(self.hboxlayout5)
        self.hboxlayout3.addLayout(self.vboxlayout6)
        self.vboxlayout4.addLayout(self.hboxlayout3)
        self.tabWidget.addTab(self.tab_2,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setContentsMargins(-1,-1,-1,10)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem)

        self.repetitionCheckBox = QtGui.QCheckBox(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repetitionCheckBox.sizePolicy().hasHeightForWidth())
        self.repetitionCheckBox.setSizePolicy(sizePolicy)
        self.repetitionCheckBox.setChecked(True)
        self.repetitionCheckBox.setObjectName("repetitionCheckBox")
        self.hboxlayout6.addWidget(self.repetitionCheckBox)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.calculateButton = QtGui.QPushButton(self.centralwidget)
        self.calculateButton.setObjectName("calculateButton")
        self.hboxlayout7.addWidget(self.calculateButton)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem2)

        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.hboxlayout7.addWidget(self.quitButton)
        self.vboxlayout.addLayout(self.hboxlayout7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,334,26))
        self.menubar.setObjectName("menubar")

        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menuInfo.addAction(self.action_About)
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.quitButton,QtCore.SIGNAL("clicked()"),MainWindow.close)
        QtCore.QObject.connect(self.spinSet,QtCore.SIGNAL("valueChanged(int)"),self.sliderSet.setValue)
        QtCore.QObject.connect(self.sliderSet,QtCore.SIGNAL("valueChanged(int)"),self.spinSet.setValue)
        QtCore.QObject.connect(self.spinSubset,QtCore.SIGNAL("valueChanged(int)"),self.sliderSubset.setValue)
        QtCore.QObject.connect(self.sliderSubset,QtCore.SIGNAL("valueChanged(int)"),self.spinSubset.setValue)
        QtCore.QObject.connect(self.permutationSpin,QtCore.SIGNAL("valueChanged(int)"),self.sliderSetPermutations.setValue)
        QtCore.QObject.connect(self.sliderSetPermutations,QtCore.SIGNAL("valueChanged(int)"),self.permutationSpin.setValue)
        QtCore.QObject.connect(self.picksSpin,QtCore.SIGNAL("valueChanged(int)"),self.sliderPicks.setValue)
        QtCore.QObject.connect(self.sliderPicks,QtCore.SIGNAL("valueChanged(int)"),self.picksSpin.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Qombinatorics", None, QtGui.QApplication.UnicodeUTF8))
        self.output.setHtml(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><span style=\" font-size:16pt; font-weight:600;\">qombinatorics</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><span style=\" font-size:10pt; font-weight:400;\">an application to calculate combination and permutation of objects</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Info: http://darkmoon.altervista.org</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Objects in set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Number of picks", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "&Permutations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Objects in set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Objects in subset", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "&Combinations", None, QtGui.QApplication.UnicodeUTF8))
        self.repetitionCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Allow &repetitions", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateButton.setText(QtGui.QApplication.translate("MainWindow", "&Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfo.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))

