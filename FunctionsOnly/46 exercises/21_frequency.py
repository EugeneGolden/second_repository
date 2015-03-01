__author__ = 'Vitaliy'
"""
Write a function char_freq() that takes a string and builds a frequency listing
of the characters contained in it. Represent the frequency listing as a Python dictionary.
Try it with something likechar_freq("abbabcbdbabdbdbabababcbcbab").
"""

def char_freq(sentence):
    my_dict = dict()
    for key in sentence:
        if key in my_dict:
            my_dict[key] = my_dict[key] + 1
        else:
            my_dict[key] = 1
    for key, val in my_dict.items():
        print key, val

char_freq("abbabcbdbabdbdbabababcbcbaba")
