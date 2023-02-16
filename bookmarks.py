class bookmark:
    
    bmList: dict = {}

    def __init__(self):
        '''Initialization of the bookmark class
            - loading the bookmarks from the file into the dictionary'''
        with open("bookmarks.txt", "r") as f:
            for line in f:
                key, value = line.split("::")
                self.bmList.update({key: value})
    def getBookmark(self):
        '''Getter of the bookmark's dictionary'''
        return self.bmList
    def bookmark(self, key, url) -> any:
        '''Adding a bookmark to the dictionary and returning the key to be added to the menu'''
        self.bmList.update({key: url})
        return key
    def saveBookmark(self):
        '''Saving the bookmarks to the file'''
        with open("bookmarks.txt", "w") as f:
            for key, value in self.bmList.items():
                f.write(key + "::" + value)
