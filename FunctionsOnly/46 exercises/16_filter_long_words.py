__author__ = 'Vitaliy'
"""
Write a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""

def filter_long_words(lst, n):
    lst_out = []
    for str in lst:
        if len(str) > n:
            lst_out.append(str)
    if len(lst_out) > 1:
        print 'The long words due to n = %d' % n, 'are', lst_out
    elif len(lst_out) == 1:
        print 'The long word due to n = %d' % n, 'is', lst_out
    else:
        print 'There are no words due to n = %d' % n

filter_long_words(['snow', 'white', 'cool', 'karamba'], 0)
