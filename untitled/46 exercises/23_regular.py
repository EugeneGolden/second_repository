"""
Define a simple "spelling correction" function correct() that takes a string and sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
E.g. correct("This   is  very funny  and    cool.Indeed!")
should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!
"""
import re
import sys

def correct(input_string):
    pattern1 = '\s\s*'                                                      #create a pattern to find 2 spaces or more
    pattern2 = '([\.\,\!\?\:\;])(\S)'                                           #create a pattern to find expressions like '.I'
    print 'Corrected sentence without spaces:', re.sub(pattern1, ' ', input_string)                               #replace a lot of space by 1 space for the 1st pattern
    print 'Find all places like .I:', re.findall(pattern2, input_string)    #find all places which look like '.I' etc. and get a list of them
    print 'The changed piece: ', split_lst(re.findall(pattern2, input_string))
    #print re.sub(pattern2, split_lst(re.findall(pattern2, input_string)), input_string )



def split_lst(found_smth):
    lst = []
    for element in found_smth: #we take a list and for every element in the list
        for char in element:  #we work with every character inside this element
            lst.append(char) # and we add the character to the new list
    return lst.insert(1,' ')   #inserts a space after the first element of the list
"""    for char in lst: #now we work with the new list and
        replace = sys.stdout.write(char) # retrieve a string for every element
    return replace"""

input_string = 'This   is  very funny  and    cool.Indeed!lki'
correct(input_string)
#pattern3 = '\s\s+|[\.\,\!\?\:\;]\S'


