from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon


def menu_bar(self):

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        helpMenu = mainMenu.addMenu('Help')


        exitbutton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitbutton.setShortcut('Ctrl+Q')
        exitbutton.setStatusTip('Exit application')
        exitbutton.triggered.connect(self.close)
        fileMenu.addAction(exitbutton)

        #options for the Help Menu
        Helpbutton = QAction(QIcon('exit24.png'), 'Help Tips', self)
        Helpbutton.setShortcut('Ctrl+H')
        Helpbutton.setStatusTip('Open Tool Help')
        Helpbutton.triggered.connect(self.help_tips)
        helpMenu.addAction(Helpbutton)