__author__ = 'Vitaliy'

"""
Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.
"""

def vowels(text):
    vow = ('a', 'e', 'i', 'o', 'u')
    result =''
    for ch in text:
        if ch in vow:
            continue
        else:
            result += ch
    return result

#print "Is this a vowel?", vowels('a', 'is it true')

print vowels('it is true')