__author__ = 'Vitaliy'
#This program delete the first and the last elements from a list
def remove_first_last(lst):
    del lst[0]
    del lst[len(lst)-1]
    return lst

t = [1, 2, 5, 8, 4, 2]
print remove_first_last(t)