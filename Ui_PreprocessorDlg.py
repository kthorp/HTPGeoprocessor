# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PreprocessorDlg.ui'
#
# Created: Thu Feb 27 11:08:50 2014
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from qgis.PyQt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreprocessorDlg(object):
    def setupUi(self, PreprocessorDlg):
        PreprocessorDlg.setObjectName(_fromUtf8("PreprocessorDlg"))
        PreprocessorDlg.resize(781, 441)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreprocessorDlg.sizePolicy().hasHeightForWidth())
        PreprocessorDlg.setSizePolicy(sizePolicy)
        PreprocessorDlg.setMinimumSize(QtCore.QSize(781, 400))
        PreprocessorDlg.setMaximumSize(QtCore.QSize(781, 471))
        self.horizontalLayoutWidget = QtGui.QWidget(PreprocessorDlg)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 400, 320, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnLoad = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.horizontalLayout_4.addWidget(self.btnLoad)
        self.btnSave = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_4.addWidget(self.btnSave)
        self.btnRun = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout_4.addWidget(self.btnRun)
        self.btnExit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout_4.addWidget(self.btnExit)
        self.label_3 = QtGui.QLabel(PreprocessorDlg)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(PreprocessorDlg)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayoutWidget = QtGui.QWidget(PreprocessorDlg)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 360, 241, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.txtEasting = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtEasting.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtEasting.setObjectName(_fromUtf8("txtEasting"))
        self.gridLayout.addWidget(self.txtEasting, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.txtNorthing = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtNorthing.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtNorthing.setObjectName(_fromUtf8("txtNorthing"))
        self.gridLayout.addWidget(self.txtNorthing, 1, 1, 1, 1)
        self.label = QtGui.QLabel(PreprocessorDlg)
        self.label.setGeometry(QtCore.QRect(10, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.txtNumCol = QtGui.QLineEdit(PreprocessorDlg)
        self.txtNumCol.setGeometry(QtCore.QRect(270, 50, 81, 20))
        self.txtNumCol.setText(_fromUtf8(""))
        self.txtNumCol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtNumCol.setObjectName(_fromUtf8("txtNumCol"))
        self.tblInstructions = QtGui.QTableWidget(PreprocessorDlg)
        self.tblInstructions.setGeometry(QtCore.QRect(10, 80, 763, 231))
        self.tblInstructions.setAlternatingRowColors(True)
        self.tblInstructions.setRowCount(50)
        self.tblInstructions.setColumnCount(9)
        self.tblInstructions.setObjectName(_fromUtf8("tblInstructions"))
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tblInstructions.setHorizontalHeaderItem(8, item)
        self.tblInstructions.horizontalHeader().setDefaultSectionSize(80)
        self.tblInstructions.verticalHeader().setVisible(True)
        self.tblInstructions.verticalHeader().setDefaultSectionSize(20)
        self.tblInstructions.verticalHeader().setMinimumSectionSize(20)
        self.progressBar = QtGui.QProgressBar(PreprocessorDlg)
        self.progressBar.setGeometry(QtCore.QRect(450, 360, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(PreprocessorDlg)
        QtCore.QMetaObject.connectSlotsByName(PreprocessorDlg)

    def retranslateUi(self, PreprocessorDlg):
        PreprocessorDlg.setWindowTitle(QtGui.QApplication.translate("PreprocessorDlg", "Sensor Data File Instructions", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoad.setText(QtGui.QApplication.translate("PreprocessorDlg", "Load File", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("PreprocessorDlg", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("PreprocessorDlg", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("PreprocessorDlg", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreprocessorDlg", "Enter the instructions for reading a comma delimited sensor data file.  Enter the sensor offsets from the GPS receiver in meters.  Assume the vehicle faces due north when entering offsets.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PreprocessorDlg", "Enter the total number of columns in the file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreprocessorDlg", "Easting:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtEasting.setText(QtGui.QApplication.translate("PreprocessorDlg", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreprocessorDlg", "Northing:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtNorthing.setText(QtGui.QApplication.translate("PreprocessorDlg", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreprocessorDlg", "Enter coordinate offset from the vehicle GPS system to the field map, if any:", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Sensor\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Latitude\n"
"Column #", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Longitude\n"
"Column #", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Heading\n"
"Column #", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Sensor ID\n"
"Column #", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Sensor ID\n"
"Text", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(6)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Data\n"
"Column #(s)", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(7)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Easting\n"
"Offset (m)", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tblInstructions.horizontalHeaderItem(8)
        item.setText(QtGui.QApplication.translate("PreprocessorDlg", "Northing\n"
"Offset (m)", None, QtGui.QApplication.UnicodeUTF8))

