__author__ = 'Tim'

a = 'ay'
o = raw_input('Enter a english Word:')
if len(o)>0 and o.isalpha():
    w = o.lower()
    f = w[0]
    n = w+f+a
    n = n[1:len(n)]
    print "Translation into Pig Latin: ",n
else:
    print 'Not a word'
