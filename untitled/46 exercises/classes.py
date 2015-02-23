__author__ = 'Admin'


class FileProcessing:
    """This class returns all lines from the file"""

    def __init__(self, f, filename="pol.txt"):
        self.filename = filename
        self.f = f

    def processFile(self):
        f = open(self.filename)
        for line in f:
            line = line.lower()
        self.f.close()



class ITextProcessing:
    """This class for text processing"""

    def __init__(self, text=None):
        self.text = text

    def char_freq(self):
        my_dict = dict()
        for key in self.text:
            if key in my_dict:
                my_dict[key] = my_dict[key] + 1
            else:
                my_dict[key] = 1