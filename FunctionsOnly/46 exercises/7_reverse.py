__author__ = 'Vitaliy'

"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""
import sys
def reverse(lst):
    for i in reversed(lst):
        sys.stdout.write(i),
    print


reverse('Im going')