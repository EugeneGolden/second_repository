"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
builds a frequency listing of the characters contained in the file, and prints a sorted and nicely
formatted character frequency table to the screen.
"""
"""
def char_freq_table(fileName):
    f = open(fileName) #open a file
    my_dict =dict() #create an empty dictionary
    lst = []
    for line in f: #start reading the file line by line
       lineLower = line.lower() #make all words in lowercase
       for word in lineLower: #we need to put every element into the list lst
           lst.append(word) #add ech element to the list
    for key in lst: #fill the dictionary with keys (characters) and values - it shows how many times characters are appeared in the file
        if key in my_dict:
            my_dict[key] = my_dict[key] + 1
        else:
            my_dict[key] = 1
    for key in sorted(my_dict):
        print key, '|', my_dict[key]

char_freq_table('pol.txt')

"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')

