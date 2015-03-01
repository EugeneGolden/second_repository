__author__ = 'Vitaliy'
"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""
import sys
def reverse(lst):
    n = len(lst) - 1
    while n >= 0:
        #sys.stdout.write(lst[n]),
        n -= 1
    print
    return lst

#reverse('123fe')

