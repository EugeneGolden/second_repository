__author__ = 'Vitaliy'
def palindrome_recognizer(palindrome):
    pal = palindrome.lower()
    pal2 = []
    for str in pal:
        if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z'):
            pal2.append(str) #compose a new list with letters only
    print pal2
    length = len(pal2)
    for i in range(len(pal2)): #To iterate over the indices of a sequence, you can combine range() and len()
        if (i <= (length - 1)): # go through the list until the lower index will be larger or equals the upper index
            if (pal2[i] == pal2[length - i - 1]): #compare the first and the last elements
                continue
            else:
                print 'They are NOT palindromes'
                exit() #as soon as our elements are not equaled then we exit the program
    print 'They are palindromes'


palindrome_recognizer('Dammit, I\'m mad!')
