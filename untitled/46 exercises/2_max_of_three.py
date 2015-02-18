__author__ = 'Vitaliy'
"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""

def max_of_three(first, second, third):
    lst = [first, second, third]
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum

print 'Maximum is', max_of_three(6,6,7)




