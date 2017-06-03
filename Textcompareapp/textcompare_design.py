# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from Textcompareapp.MenuBar import menu_bar

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setObjectName("MainWindow")
        self.resize(487, 434)
        self.setMinimumSize(QtCore.QSize(487, 434))
        self.setMaximumSize(QtCore.QSize(487, 434))
        self.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.compareButton = QtWidgets.QPushButton(self.centralwidget)
        self.compareButton.setEnabled(False)
        self.compareButton.setGeometry(QtCore.QRect(190, 350, 101, 31))
        self.compareButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.compareButton.setStatusTip("")
        self.compareButton.setObjectName("compareButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 29, 341, 21))
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.fileoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileoneButton.setGeometry(QtCore.QRect(380, 22, 91, 31))
        self.fileoneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileoneButton.setObjectName("fileoneButton")
        self.filetwoButton = QtWidgets.QPushButton(self.centralwidget)
        self.filetwoButton.setGeometry(QtCore.QRect(380, 62, 91, 31))
        self.filetwoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filetwoButton.setWhatsThis("")
        self.filetwoButton.setObjectName("filetwoButton")
        self.comparison_label = QtWidgets.QLabel(self.centralwidget)
        self.comparison_label.setGeometry(QtCore.QRect(20, 110, 141, 31))
        self.comparison_label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.comparison_label.setObjectName("comparison_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 150, 451, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Text Comparison Tool"))
        self.setToolTip(_translate("MainWindow", "Select first file for comparision"))
        self.compareButton.setToolTip(_translate("MainWindow", "Click to compare selected files"))
        self.compareButton.setText(_translate("MainWindow", "Compare"))
        self.fileoneButton.setStatusTip(_translate("MainWindow", "Click to choose file"))
        self.fileoneButton.setText(_translate("MainWindow", "Select File 1"))
        self.filetwoButton.setToolTip(_translate("MainWindow", "Select second file for comparision"))
        self.filetwoButton.setStatusTip(_translate("MainWindow", "Click to choose file"))
        self.filetwoButton.setText(_translate("MainWindow", "Select File 2"))
        self.comparison_label.setText(_translate("MainWindow", "<span style=\" font-size:10pt; font-weight:600;\">Comparision Result:</span>"))

        # Addign menu bar
        menu_bar(self)

        # Selection File One
        self.fileoneButton.clicked.connect(lambda: self.file_selection(1))

        # Selecting File Two
        self.filetwoButton.clicked.connect(lambda: self.file_selection(2))

        # Comparing the two files
        self.compareButton.clicked.connect(self.comparision_action)

    @pyqtSlot()
    def file_selection(self,clicked_value):
        from Textcompareapp.ChooseFile import choose_image
        choose_image(self,clicked_value)

    @pyqtSlot()
    def comparision_action(self):

        from Textcompareapp.Comparsion import FileCompare

        FileCompare.comparision_tool(self)

    @pyqtSlot()
    def help_tips(self):
        help_msg = '''
This tool will help you to compare the selected files and shows the     comparision data.
            1. Select the two file whose text you want to compare.
            2. Click on Compare button
            3. The selected files will be compared and the comparision results will be
               shown
            '''
        QtWidgets.QMessageBox.question(self, 'Help - Image Text Extractor', help_msg, QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())

