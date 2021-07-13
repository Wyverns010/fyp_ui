# import PyQt5

# print(PyQt5.__version__)
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from PyQt5.QtWebKit import * 
# from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
# from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# app = QApplication(sys.argv)
def gameTabWidget():
    webApp = QWebView()
    filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "game/index.html"))
    local_url = QUrl.fromLocalFile(filePath)
    webApp.load(local_url)
    return webApp

# webApp.show()

# sys.exit(app.exec_())