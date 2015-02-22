__author__ = 'Admin'

class FileProcessing:
    'This class returns all lines from the file'
    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def openFile(self):
        return open(self.filename)