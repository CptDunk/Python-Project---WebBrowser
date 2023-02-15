from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from bookmarks import *
import sys

class MyWebBrowser(QMainWindow):
    
    bookmarks = bookmark()

    def __init__(self):
        super(MyWebBrowser, self).__init__()


        self.window = QWidget()
        self.window.setWindowTitle("Simple Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        
        self.go_btn = QPushButton("Go") 
        self.go_btn.setMinimumHeight(30)
        
        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)
        
        self.forw_btn = QPushButton("Forward")
        self.forw_btn.setMinimumHeight(30)

        self.save_btn = QPushButton("Save")
        self.save_btn.setMinimumHeight(30)
        self.save_btn.setMaximumWidth(45)

        self.bmMenu = QMenu()
        for key in self.bookmarks.getBookmark():
            action = self.bmMenu.addAction(key)
            action.triggered.connect(lambda chk, item = key: self.navigate(self.bookmarks.getBookmark()[item].strip()))

       
        self.bmBtn = QPushButton("Bookmarks")
        self.bmBtn.setMinimumHeight(30)
        self.bmBtn.setMenu(self.bmMenu)
        
        self.horizontal.addWidget(self.save_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forw_btn)
        self.horizontal.addWidget(self.bmBtn)
        
        self.browser = QWebEngineView()
        
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.back_btn.clicked.connect(lambda: self.browser.back())
        self.forw_btn.clicked.connect(lambda: self.browser.forward())
        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))
        self.browser.loadProgress.connect(lambda: self.refreshURL())
        self.save_btn.clicked.connect(lambda: self.gettext(self.url_bar.text()))


        

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        self.window.setLayout(self.layout)
        self.window.closeEvent = self.closeEvent
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http") and not url.startswith("https"):
            url = "http://" + url
            self.url_bar.setText(url)
            self.url_bar.setCursorPosition(0)
        self.browser.setUrl(QUrl(url))

    def gettext(self, url):
      text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
      if ok:
            self.bookmarks.bookmark(text, url)
            print("success")
    
   
    
        
    def closeEvent(self, event):
        print("Closing Application...")
        self.bookmarks.saveBookmark()
        super().closeEvent(event)

    def refreshURL(self):
        self.url_bar.setText(self.browser.url().toString())
        self.url_bar.setCursorPosition(0)
    

