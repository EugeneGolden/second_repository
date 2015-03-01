__author__ = 'Vitaliy'

"""
Write a function translate() that will translate a text into (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon".
"""
import sys
Print = sys.stdout.write
vow = ('a', 'e', 'i', 'o', 'u')
cons = ('b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
def translate(sentence):
    for i in sentence:
        if i in cons:
            sys.stdout.write(i + 'o' + i),
        elif i == '':
            print ' ',
        else:
            sys.stdout.write(i),


print translate('by the way')


