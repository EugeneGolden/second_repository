__author__ = 'Admin'

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

    def filterText(self, text ):
        if (len(text) > 10):
            #print "OnlyLongLinesFilter ALLOWED: " + text
            return text.lower()
        else:
            print "OnlyLongLinesFilter BLOCKED: " + text
            return ''
