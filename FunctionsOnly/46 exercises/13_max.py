"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two
and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot
tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and
returns the largest one.
"""

def max_in_list(lst):
    maxi = lst[0]
    print maxi
    for i in lst:
        if i > maxi:
            maxi = i
            print 'Max is', maxi
    print 'Final max is', maxi

lst2 = [4, 3, 5, 6, 1, 0, -1, 8, 3, 2]
max_in_list(lst2)



