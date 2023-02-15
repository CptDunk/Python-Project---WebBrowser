class bookmark:
    
    bmList: dict = {}

    def __init__(self):
        with open("bookmarks.txt", "r") as f:
            for line in f:
                key, value = line.split("::")
                self.bmList.update({key: value})
    def getBookmark(self):
        return self.bmList
    def bookmark(self, key, url, dict,):
        dict.update({key: url})
        action = self.bmMenu.addAction(key)
        action.triggered.connect(lambda chk, item = key: self.navigate(dict[item]))
    def saveBookmark(self):
        with open("bookmarks.txt", "w") as f:
            for key, value in self.bmList.items():
                f.write(key + "::" + value)