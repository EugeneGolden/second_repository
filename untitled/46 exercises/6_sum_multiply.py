__author__ = 'Vitaliy'

"""
Define a function sum() and a function multiply() that sums and multiplies (respectively)
all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.
"""
array = [4,5,6]

def sum_numbers(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def multiply(lst):
    multipl = 1
    for i in lst:
        multipl *= i
    return multipl

print "Sum is", sum_numbers(array)
print "Multiply is", multiply(array)