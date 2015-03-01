__author__ = 'Vitaliy'
"""
Using the higher order function filter(), define a function filter_long_words()
that takes a list of words and an integer n and returns the list of words that are longer than n.
"""
lst = ['bright', 'bus', 'cool', 'superman']

def f(lst): return len(lst) > 3

print filter(f, lst)