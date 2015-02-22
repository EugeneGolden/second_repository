__author__ = 'Admin'

class FileReading:
    'This class returns all lines from the file'
    def __init__(self, filename):
        self.filename = filename

    def openFile(self):
        return open(self.filename)