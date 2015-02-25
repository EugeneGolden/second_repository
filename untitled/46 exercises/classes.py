__author__ = 'Admin'


class FileProcessor:
    """This class returns all lines from the file"""

    def __init__(self, filename="pol.txt"):
        self.filename = filename

    def processFile(self):
        f = open(self.filename)
        for line in f:
            line = line.lower()
            #really don't know how to put ITextReceiver.receiver here
        f.close()

class ITextReceiver:
    """This class accepts text"""

    def __init__(self, text=None):
        self.text = text

    def receiver(self, text):
        pass


class WordCount:
    """This class for counting words"""

    def __init__(self, text=None):
        self.text = text

    def char_freq(self):
        my_dict = dict()
        for key in self.text:
            if key in my_dict:
                my_dict[key] = my_dict[key] + 1
            else:
                my_dict[key] = 1
