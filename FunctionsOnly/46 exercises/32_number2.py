__author__ = 'Vitaliy'
"""
Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.
"""



def palindrome(filename):
   f = open(filename)
   for line in f:
       lineLower = line.lower()
       print lineLower
       palLetters = []
       for str in lineLower:
           if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z'):
               palLetters.append(str) #compose a new list with letters only. It was removed all other characters but letters
       first = 0 #a number for the first element
       last = len(palLetters) #will use for a number for the last element
       print palLetters
       isPalindrome = True
       while first <= last:
           if palLetters[first] == palLetters[last-1]:
               first += 1
               last -= 1
           else:
               isPalindrome = False
               break
       if isPalindrome == False:
           print 'The sentence is NOT a palindrome'
           continue
       else:
           print "This is a palindrome"

palindrome('pol.txt')
