__author__ = 'Vitaliy'

"""
Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.
"""
import basicFunctions
#from eight_polindrome import isPolindrome

def palindrome(filename):
    f = open(filename)
    for line in f:
        listLetters = basicFunctions.makeLettersLowercase(line)
        result = basicFunctions.isPolindrome(listLetters)
        if result == False:
            print 'The sentence is NOT a palindrome'
            continue
        else:
            print "This is a palindrome"


palindrome('pol.txt')

"""
pol.txt:
Dammit, I\'m mad!
Dammit, I\'m mad!jk;lk
Dammit, I\'m mad!Dammit, I\'m mad!
"""

