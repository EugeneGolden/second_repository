__author__ = 'Vitaliy'
"""
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words.
"""

def map(lst):
    lst_numbers = []
    for i in lst:
        element = len(i)
        lst_numbers.append(element)
    print 'Our new list is', lst_numbers

map(['cool', 'wonderful', 'tree'])

