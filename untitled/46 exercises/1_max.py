__author__ = 'Vitaliy'
"""
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def max_function(first, second):
    if first > second:
        maximum = first
    else:
        maximum = second
    return maximum

print 'Maximum between the number equals', max_function(58,3)
