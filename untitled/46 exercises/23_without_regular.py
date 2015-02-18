__author__ = 'Vitaliy'
"""
Define a simple "spelling correction" function correct() that takes a string and sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
E.g. correct("This   is  very funny  and    cool.Indeed!")
should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!
"""

def remove_spaces(sentence):
    new_sentence = ''
    for i in range(0, len(sentence)-1):
        if (sentence[i] == ' ') and (sentence[i+1] == ' '):
            continue
        else:
            new_sentence = new_sentence + sentence[i]
    new_sentence = new_sentence + sentence[len(sentence)-1]
    return new_sentence



def insert_space(sentence):
    new_sentence = ''
    for i in range(0, len(sentence)-1):
        if (sentence[i] in ['.', ',', '!', '?', ';', ':']) and (sentence[i+1] != ' '):
            new_sentence = new_sentence + sentence[i] + ' '
        else:
            new_sentence = new_sentence + sentence[i]
    new_sentence = new_sentence + sentence[len(sentence)-1]
    return new_sentence

sentence = 'This   is  very funny  and    cool.Indeed!dsf,asd '
withoutSpaces = remove_spaces(sentence)
withoutSpacesAndWithInsertedOnes = insert_space(withoutSpaces)
print withoutSpacesAndWithInsertedOnes

