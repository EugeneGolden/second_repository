__author__ = 'Vitaliy'
"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets",
"Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
"""

def palindrome_recognizer(palindrome):
    palindrome = palindrome.lower()
    palindrome2 = palindrome[::-1]
    pal = palindrome.split()
    pal2 = palindrome2.split()
    print pal
    print pal2
    pal =  ''.join(pal)
    print pal
    pal2 = ''.join(pal2)
    print pal2
    if pal == pal2:
        print 'They are palindromes!'
    else:
        print 'They are NOT palindromes'


palindrome_recognizer('Was it a rat I saw')
