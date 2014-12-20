__author__ = 'Tim'
import operator
ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.div}
a = ""
f = float(input("Insert first Number: "))
op_char = raw_input("Insert operator [+,-,*,/]: ")
l = (input("Insert second Number: "))
op_func = ops[op_char]
x = op_func(f, l)
print x

