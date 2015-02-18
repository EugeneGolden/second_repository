__author__ = 'Vitaliy'
import reverse

"""
Define a function is_palindrome() that recognizes palindromes
(i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""

def isPolindrome(lst):
    lst_mirror = lst[::-1]
    if lst == lst_mirror:
        return True
    else:
        return False

isPolindrome('n abba abba n')

"""
Compose a new list with letters only. It was removed all other characters but letters
"""
def makeLettersLowercase(line):
    lineLower = line.lower()
    #print lineLower
    palLetters = []
    for str in lineLower:
        if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z'):
            palLetters.append(str)
    return palLetters

"""
"""
#Compose a new list with all characters
"""
def makeListLowercase(line):
    lst = []
    lineLower = line.lower() #make all words in lowercase
        for word in lineLower: #we need to put every element into the list lst
            lst.append(word) #add ech element to the list
    return lst
"""
#How this piece of code to insert into 34
#print makeLettersLowercase('Passage sdafH,,,,')
"""
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
        """

"""
Fill the dictionary with keys (characters) and values - it shows how many times characters are appeared in the file
"""
def dictShowsTimes(lst):
    my_dict =dict()
    for key in lst:
       if key in my_dict:
           my_dict[key] = my_dict[key] + 1
       else:
           my_dict[key] = 1
    return my_dict

