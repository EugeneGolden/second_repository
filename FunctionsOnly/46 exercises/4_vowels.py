__author__ = 'Vitaliy'

"""
Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.
"""

def vowels(ch):
    vow = ('a', 'e', 'i', 'o', 'u')
    #for i in vow:
    if ch in vow:
        result = True
    else:
        print 'False'
    return result

print "Is this a vowel?", vowels('a')