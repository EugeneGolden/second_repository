__author__ = 'Vitaliy'
"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.
"""
def pangram(sentence):
    sentence = sentence.lower()
    sentence_new = []
    my_dict = dict()
    for str in sentence:
       if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z'):
           sentence_new.append(str) #compose a new list with letters only. It was removed all other characters but letters
    for str in sentence_new:
        if str in my_dict:
            my_dict[str] = my_dict[str] + 1
        else:
            my_dict[str] = 1
    print my_dict
    print len(my_dict)
    if len(my_dict) == 26: # this value equals amount of letters an the alphabet
        print "This sentence is a pangram"
    else:
        print 'This is NOT a pangram'

pangram('The quick brown fox jumps over the lazy dog.')
