__author__ = 'Vitaliy'
my_file = open('mbox-short.txt', 'r')
for line in my_file:
    line = line.upper()
    print line

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print days[2]
