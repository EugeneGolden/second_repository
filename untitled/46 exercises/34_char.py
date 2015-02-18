__author__ = 'Admin'
"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
builds a frequency listing of the characters contained in the file, and prints a sorted and nicely
formatted character frequency table to the screen.
"""
import basicFunctions

def char_freq_table(fileName):
   f = open(fileName) #open a file
   lst = []
   for line in f: #start reading the file line by line
      lineLower = line.lower() #make all words in lowercase
      for word in lineLower: #we need to put every element into the list lst
          lst.append(word) #add ech element to the list
   my_dict = basicFunctions.dictShowsTimes(lst)
   for key in sorted(my_dict):
       print key, '|', my_dict[key]

char_freq_table('pol.txt')
