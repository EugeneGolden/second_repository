__author__ = 'Admin'

class FileProcessor:
    """This class returns line by line from the file"""

    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def processFile(self):
        f = open(self.filename)
        for line in f:
            IReceiver.receiver(line)
        f.close()

class IReceiver:
    """This class for counting words"""

    my_dict = dict()
    def receiver(self, line):
        for key in self.line:
            if key in self.my_dict:
                 self.my_dict[key] =  self.my_dict[key] + 1
            else:
                 self.my_dict[key] = 1

    def getDict(self):
        return self.my_dict


fp = FileProcessor("pol.txt")
fp.processFile()
