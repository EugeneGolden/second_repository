__author__ = 'Vitaliy'
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.split()
    if len(line) < 2 : continue
    if line[0] != 'From':
        continue
    hour = line[5].split(':')
    hour = hour[0]
   # print 'Hour is', hour
    counts[hour] = counts.get(hour, 0) +1
    #print counts[hour]

lst = list()
for val, key in counts.items():
    lst.append( (val, key) )
lst.sort()

for val, key in lst:
    print val, key
