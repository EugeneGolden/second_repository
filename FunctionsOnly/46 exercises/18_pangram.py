__author__ = 'Vitaliy'
"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.
"""
def pangram(sentence):
    my_dict = dict()
    sentence = sentence.lower()
    for str in sentence:
        if str in my_dict:
            my_dict[str] = my_dict[str] + 1
        else:
            my_dict[str] = 1
    print my_dict
    for val, key in my_dict.items():
        if key == 1:
            continue
        else:
            print "This sentence is NOT a pangram"
            exit()
    print "This sentence is a pangram"

pangram('The quickt')


