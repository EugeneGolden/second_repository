__author__ = 'Vitaliy'
"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example,histogram([4, 9, 7]) should print the following:
****
*********
*******
"""
import sys

def histogram(lst):
    for i in lst:
        print
        for j in range(0,i):
            sys.stdout.write('*')

histogram([2,4,3])
