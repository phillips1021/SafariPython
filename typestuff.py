x = "Hello"
print(x)
print(type(x))

# x = 1e308
x = 2000000000 # literal forms for binary, hexadecimal, complex numbers!!
# x = x ** x  # int type is "unbounded", this would a) take ages, b) probably run out of memory
print(x)
print(type(x))

s1 = "Hello"
s2 = " World"
print(s1 + s2)
x = 99
print(s1 + str(x))  # str delegates to the __str__ method in the str class.

print(s1 * 3)

x = 10
y = 3
print(x / y)
print(x // y)
print(x)
print(type(x))

# import math
# tup = math.modf(3.141)  # result is a tuple??!!

from math import modf
tup = modf(3.141)  # result is a tuple??!!

print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
print(len(tup))

from random import random as rnd
# print(random())
print(rnd())

