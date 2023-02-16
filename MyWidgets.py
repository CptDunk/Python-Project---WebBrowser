from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from bookmarks import *
import sys

class MyWebBrowser(QMainWindow):
    
    bookmarks = bookmark()

    def __init__(self):
        '''Initialization of the main window and its components/widgets, as well as the layout
            - creating the main window
            - setting the layout
            - calling __init__ method of bookmarks class'''
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
        self.browser.loadFinished.connect(lambda: self.refreshURL())
        self.save_btn.clicked.connect(lambda: self.gettext(self.url_bar.text()))


        

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        self.window.setLayout(self.layout)
        self.window.closeEvent = self.closeEvent
        self.window.show()

    def navigate(self, url):
        '''This method is called when the user clicks on the Go button or presses the Enter key while the url_bar is selected/active.
            It checks if the url starts with http or https, if not, it adds http:// to the beginning of the url and then loads the url in the browser.'''
        if not url.startswith("http") and not url.startswith("https"):
            url = "http://" + url
            self.url_bar.setText(url)
            self.url_bar.setCursorPosition(0)
        self.browser.setUrl(QUrl(url))

    def gettext(self, url):
      '''This method is called when the user clicks on the Save button, which brings up a dialog box where the user can enter the name of the bookmark.
            It then calls the bookmark method of the bookmark class and passes the name and url of the bookmark as parameters.
            '''
      text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'How will you name your bookmark?:')
      if ok:
            key = self.bookmarks.bookmark(text, url)
            action = self.bmMenu.addAction(key)
            action.triggered.connect(lambda chk, item = key: self.navigate(self.bookmarks.getBookmark()[item].strip()))

    def closeEvent(self, event):
        '''This method is called when the user clicks on the close button of the main window.
            It calls the saveBookmark method of the bookmark class and then closes the application.'''
        print("Closing Application...")
        self.bookmarks.saveBookmark()
        super().closeEvent(event)

    def refreshURL(self):
        '''This method is called when the starts loading new page or when the page is fully loaded.
            It sets the text of the url_bar to the url of the page that is currently loaded in the browser.'''
        self.url_bar.setText(self.browser.url().toString())
        self.url_bar.setCursorPosition(0)
    

