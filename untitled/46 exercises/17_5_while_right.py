def palindrome_recognizer(palindrome):
   pal = palindrome.lower()
   pal2 = []
   for str in pal:
       if str in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','q','v','w','x','y','z'):
           pal2.append(str) #compose a new list with letters only. It was removed all other characters but letters
   #print pal2
   first = 0 #a number for the first element
   last = len(pal2) #will use for a number for the last element
   while first <= last:
       if pal2[first] == pal2[last-1]:
           first += 1
           last -= 1
       else:
           print 'The sentence is NOT a palindrome'
           exit()
   print 'The sentence is a palindrome'

palindrome_recognizer('Dammit, I\'m mad!')

