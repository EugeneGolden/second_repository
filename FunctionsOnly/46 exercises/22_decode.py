def decode(cipher, lst):
   uncode = ''
   for i in lst:
       if cipher.has_key(i):
           value = cipher.get(i)
           uncode += value
       elif i == ' ':
           uncode += i
   return uncode


"""
def code(cipher, lst):
    coded = ''
    mirror_cipher = dict()
    for key, val in cipher.items():
        mirror_cipher.update({val:key})
    for i in lst:
        if mirror_cipher.has_key(i):
            value = cipher.get(i)
            coded += value
        elif i == ' ':
            coded += i
    return coded
"""

def code(cipher, lst):
#    coded = ''
    mirror_cipher = dict()
    for key, val in cipher.items():
        mirror_cipher.update({val:key})
    coded_line = decode(mirror_cipher, lst)
    return coded_line


"""
def code(cipher, lst):
    mirror_cipher = dict()
    for key, val in cipher.items():
        mirror_cipher.update({val:key})
    return mirror_cipher
"""

cipher = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
      'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
      'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
      'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
      'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
      'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
      'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

print decode(cipher, 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')  #Caesar cipher I much prefer Caesar salad    Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

#print code(cipher, 'Caesar cipher I much prefer Caesar salad')
