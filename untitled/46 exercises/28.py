__author__ = 'Vitaliy'
"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
Use only higher order functions.
"""

lst = ['bright', 'bus', 'cool', 'superman']
f = lambda a,b: a if len(a) > len(b) else b
print reduce(f, lst)
