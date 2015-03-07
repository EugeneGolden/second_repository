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


class WordsCalculator:
    """This class for counting words"""
    my_dict = dict()

    def receive(self, line):
        print "WordsCalculator receive: " + line
        #line = line.split() #split words to have elements of a list
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
        filteredtext = self.filterText( text )
        self.adaptor.receive( filteredtext )

    def filterText(self, text ):
        return text


class LowerCaseFilter(AbstractFilter):
    """This class makes all words lowercase"""
    #TODO: how to write constructor in case of inheritance

    def filterText(self, text ):
        filteredtext = text.lower()
        #print "LowerCaseFilter converted: " + text + "  into  " + filteredtext
        return filteredtext

class RemoveVowels(AbstractFilter):
    """This class removes all vowels from text"""

    def filterText(self, text):
        vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
        filteredtext =''
        for ch in text:
            if ch in vowels:
                continue
            else:
                filteredtext += ch
        return filteredtext

class OnlyLongLinesFilter(AbstractFilter):
    """This class makes all words lowercase"""
    #TODO: how to write constructior in case of inheritance

    def filterText(self, text ):
        if (len(text) > 10):
            #print "OnlyLongLinesFilter ALLOWED: " + text
            return text.lower()
        else:
            print "OnlyLongLinesFilter BLOCKED: " + text
            return ''


filename = "pol.txt"
fp = FileProcessor(filename)
wc = WordsCalculator()
#fp.processFile(wc)
#lwc = LowerCaseFilter( wc )
#filterforwc = OnlyLongLinesFilter( lwc )
#fp.processFile(filterforwc)
#filterforwc = OnlyLongLinesFilter( wc )
#fp.processFile( filterforwc )
#lwc = LowerCaseFilter( wc )
#ollf = OnlyLongLinesFilter( lwc );
#fp.processFile( ollf )
rw = RemoveVowels( wc )
fp.processFile( rw )
print "This is results of words counting regarding file %s:" % filename, wc.getDict()

