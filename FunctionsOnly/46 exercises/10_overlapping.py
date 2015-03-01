__author__ = 'Vitaliy'
"""
Define a function overlapping() that takes two lists and returns True
if they have at least one member in common, False otherwise.
You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
"""
def overlapping(lst1, lst2):
    dic = dict()
    for i in lst1:
        for j in lst2:
            if i == j:
                print 'We have', i, 'as common parts'
                if i in dic:
                    dic[i] = dic[i] + 1
                    print dic
                else:
                    dic[i] = 1
                    print dic




overlapping('oog', 'hhhhhh')

