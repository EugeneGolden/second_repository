__author__ = 'Admin'

class FileProcessor:
    """This class returns line by line from the file"""

    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def processFile(self, calculator):
        f = open(self.filename)
        for line in f:
            #print "processFile: " + line
            calculator.receive(line)
        f.close()
