__author__ = 'Vitaliy'
"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""
list1 = [3, 4, 1, 8]

def length(lst):
    count = 0
    for i in lst:
        count += 1
    return count

print "Length of the list is", length(list1)
