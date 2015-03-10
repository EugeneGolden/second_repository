__author__ = 'Admin'

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
