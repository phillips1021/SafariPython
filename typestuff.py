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

print(x, y, x == y, x != y)

x += 10
# x++ # NOPE not in Python!!
print(x := 99)  # "walrus" operator is assignment, but is also an *expression*, value is what's assigned
print(x)

a = "Hello"
x = "Hello"
y = "He"
print(x == y)  # delegates to __eq__
y = y + "llo"
print(x == y)

print(x is y)
print(x is a)

b = "99"
print(b == 99)
print(b == str(99))
print(int(b) == 99)

# msg = input()
msg = input("Hello, please enter text: ")
# print("You entered", msg, sep="xxxx", end="ENDENDEND")
print("You entered", msg, sep=" ", end="\n")  # single space and newline are defaults for these!
print("Thanks, we're done")
