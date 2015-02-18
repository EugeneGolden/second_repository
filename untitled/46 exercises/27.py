__author__ = 'Vitaliy'
"""
Write a program that maps a list of words into a list of integers representing the lengths
of the correponding words. Write it in three different ways:
1) using a for-loop,
2) using the higher order function map(), and
3) using list comprehensions.
"""

def string_to_integers(lst):
    lst_integers = []
    for str in lst:
        lst_integers.append(len(str))
    return lst_integers

lst = ['bright', 'bus', 'cool']
print string_to_integers(lst)

print map(lambda a: len(a), lst)

str_to_int = [len(str) for str in lst]
print str_to_int
