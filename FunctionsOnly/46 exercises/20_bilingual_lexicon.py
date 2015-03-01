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
    translation = []
    for i in lst:
        for val, key in dictionary.items():
            if i == val:
                translation.append(i)
    for i in translation:
            print i,


translate({"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"er"}, ["merry", "christmas","and", "happy", "new", "year"])


