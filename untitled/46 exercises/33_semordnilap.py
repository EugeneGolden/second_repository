__author__ = 'Vitaliy'
"""
According to Wikipedia, a semordnilap is a word or phrase that spells a different
word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
from the user and finds and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the output should include
the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
"""
def semordnilap(filename):
    f = open(filename) #open a file
    my_dict =() #create an empty dictionary
    lst = [] #create an empty list
    for line in f: #start reading the file line by line
        lineLower = line.lower() #make all words in lowercase
        splitted =  line.split() #split words to have elements of a list
        for word in splitted: #we need to put every element into the list lst. If we put all line then we would have a list into the list
            lst.append(word) #add ech element to the list
    start = 0
    for str in lst: #now start working with the list after all words of the file have been added
        str_mirror = str[::-1] #make each element of the list mirror
        #print str_mirror
        start += 1
        for i in range(start, len(lst)):
            if str_mirror == lst[i]:
                my_dict = {str:lst[i]}
                print my_dict
    return my_dict

semordnilap('pol.txt')
