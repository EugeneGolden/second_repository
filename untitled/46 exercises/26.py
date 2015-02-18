__author__ = 'Vitaliy'
"""
Using the higher order function reduce(), write a function max_in_list()
that takes a list of numbers and returns the largest one.
Then ask yourself: why define and call a new function, when I can just as well call the reduce()
function directly?
"""

lst = [2,3,1,9,4]
f = lambda a, b: a if (a > b) else b
print reduce(f, lst)
