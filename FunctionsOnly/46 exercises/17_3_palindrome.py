__author__ = 'Vitaliy'
def palindrome_recognizer(palindrome):
    pal = palindrome.lower()
    pal2 = []
    for str in pal:
        if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','q','v','w','x','y','z'):
            pal2.append(str) #compose a new list with letters only
    first = 0
    last = len(pal2)
    count = 0
    middle = last / 2
    for i in pal2:
        first_el = i
        print 'First_el IS', first_el
        for j in reversed(pal2):
            print 'last - j IS', j
            if first_el == j:
                print "Cool!"
                break

palindrome_recognizer('Dammit, I\'m mad!')