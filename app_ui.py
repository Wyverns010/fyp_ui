from widgets_util import gameTabWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTabWidget, \
                            QGridLayout, QVBoxLayout, QMainWindow
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings


class AppUI(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)

        mainLayout = QGridLayout()
        vLayout1 = QVBoxLayout()
        
        # game section
        self.gameTab = QWidget()
        self.gameTab.layout = QVBoxLayout()
        self.gameTab.layout.addWidget(gameTabWidget())
        self.gameTab.layout.addWidget(QLabel('action: '))
        self.gameTab.layout.addWidget(QLabel('calories burned: '))

        self.gameTab.setLayout(self.gameTab.layout)

        # camera section
        self.cameraTab = QWidget()
        self.cameraTab.layout = QVBoxLayout()
        self.cameraTab.layout.addWidget(gameTabWidget())
        # self.cameraTab.layout.addWidget(QLabel('action: '))
        # self.cameraTab.layout.addWidget(QLabel('calories burned: '))

        self.cameraTab.setLayout(self.cameraTab.layout)


        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.gameTab, 'game')  

        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.cameraTab, 'camera')      
        
        mainLayout.addWidget(self.tabs1,0, 0)
        mainLayout.addWidget(self.tabs2,0, 1)
        self.setLayout(mainLayout)





app = QApplication(sys.argv)
appEntry = AppUI()
appEntry.show() 


sys.exit(app.exec_())