__author__ = 'Vitaliy'
"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example,histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

def histogram(lst):
    str = ''
    for i in lst:
        print str
        str = ''
        for j in range(0,i):
            str += '*'
    print str



histogram([2,4,3])
