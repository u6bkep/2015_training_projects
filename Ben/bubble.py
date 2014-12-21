#!/usr/bin/python
__author__ = 'ben'
import sys
a = open(sys.argv[1], 'r')
b = []
number_list = a.readlines()


for line in number_list:
    b.append(int(line))

b.sort()

for x in b:
    print x

a.close()