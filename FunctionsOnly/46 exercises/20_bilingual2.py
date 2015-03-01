__author__ = 'Vitaliy'
# coding: utf-8

"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"er"
and use it to translate your Christmas cards from English into Swedish. That is, write a
function translate() that takes a list of English words and returns a list of Swedish words.
"""
import sys

def translate(dictionary, lst):
    translation = ''
    for i in lst:
        if dictionary.has_key(i):
            value = dictionary.get(i)
            translation += (value + ' ')
    return translation




print translate({"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"er"}, ["merry", "christmas","and", "happy", "new", "year"])


"""
def translate(dictionary, lst):
    translation = []
    for i in lst:
        if dictionary.has_key(i):
            value = dictionary.get(i)
            translation.append(value)
    print translation
"""
