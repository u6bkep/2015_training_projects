__author__ = 'ben'

import sys

if sys.argv[1] > 0 and sys.argv[1].isalpha():
    atinlay = sys.argv[1]
    a = atinlay[0]
    b = atinlay[1:]
    atinlay = b+a+'ay'
    print atinlay
else:
    print "invalid string"