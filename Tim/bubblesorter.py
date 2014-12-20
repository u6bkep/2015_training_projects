__author__ = 'Tim'
a = open("bubble.txt", "r")
i = []
for val in a.read().split():
    i.append(int(val))
a.close()
print " Not sorted: ",i
i.sort()
print " sorted: ",i

