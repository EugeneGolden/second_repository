class FileProcessor:
    """This class returns line by line from the file"""

    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def processFile(self, calculator):
        f = open(self.filename)
        for line in f:
            calculator.receive(line)
        f.close()

class WordsCalculator:
    """This class for counting words"""

    my_dict = dict()
    def receive(self, line):
        for key in line:
            if key in self.my_dict:
                self.my_dict[key] = self.my_dict[key] + 1
            else:
                self.my_dict[key] = 1

    def getDict(self):
        return self.my_dict

fp = FileProcessor("pol.txt")
wc = WordsCalculator()
fp.processFile(wc)
print wc.getDict()
