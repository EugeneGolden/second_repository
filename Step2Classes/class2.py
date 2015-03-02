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
        line = line.split() #split words to have elements of a list
        for key in line:
            if key in self.my_dict:
                self.my_dict[key] = self.my_dict[key] + 1
            else:
                self.my_dict[key] = 1
    #It seems I need to put this method into a separate class

    def getDict(self):
        return self.my_dict


class AbstractFilter:
    def __init__(self, adaptor):
        self.adaptor = adaptor

    def receive(self, text):
        self.adaptor.receive( self.filterText( text) )

    def filterText(self, text ):
        return text


class LowerCaseFilter(AbstractFilter):
    """This class makes all words lowercase"""
    #TODO: how to write constructor in case of inheritance
    def filterText(self, text ):
        return text.lower()


class OnlyLongLinesFilter(AbstractFilter):
    """This class makes all words lowercase"""
    #TODO: how to write constructior in case of inheritance
    def filterText(self, text ):
        if (len(text) > 10):
            return text.lower()
        else:
            return ''


filename = "pol.txt"
fp = FileProcessor(filename)
wc = WordsCalculator()
fp.processFile(wc)
fp.processFile( LowerCaseFilter( wc ) )
fp.processFile( OnlyLongLinesFilter( wc ) )
fp.processFile( OnlyLongLinesFilter( LowerCaseFilter(wc) ) )
print "This is results of words counting regarding file %s:" % filename, wc.getDict()


