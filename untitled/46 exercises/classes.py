class FileProcessor:
    """This class returns line by line from the file"""

    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def processFile(self, calculator):
        f = open(self.filename)
        for line in f:
            calculator.receive(line)
        f.close()

class LettersCalculator:
    """This class for counting letters"""

    my_dict = dict()
    def receive(self, line):
        for key in line:
            if key in self.my_dict:
                self.my_dict[key] = self.my_dict[key] + 1
            else:
                self.my_dict[key] = 1

    def getDict(self):
        return self.my_dict

class WordsCalculator:
    """This class for counting words"""

    my_dict = dict()
    def receive(self, line):
        line = line.split() #split words to have elements of a list
        for key in line:
            if key in self.my_dict:
                self.my_dict[key] = self.my_dict[key] + 1
            else:
                self.my_dict[key] = 1
    #It seems I need to put this method into a separate class
    def getDict(self):
        return self.my_dict

class CountWords:
    """This class for counting words"""

    count = 0
    def receive(self, line):
        line = line.split()
        for word in line:
            self.count +=1

    def getCount(self):
        return self.count

filename = "pol.txt"
fp = FileProcessor(filename)

lc = LettersCalculator()
fp.processFile(lc)
print "This is results of letters counting regarding file %s:" % filename, lc.getDict()

wc = WordsCalculator()
fp.processFile(wc)
print "This is results of words counting regarding file %s:" % filename, wc.getDict()

cw = CountWords()
fp.processFile(cw)
print "Amount of words into the file %s is" % filename, cw.getCount()
