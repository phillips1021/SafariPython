
# tup = ("one", 2, 3.0)
tup = "one", 2, 3.0
print(tup)
print(tup[1])
# tuple structure is not modifiable (if contents are mutable objects,
# yes you can change them!!!!
# tup[1] = 99
# print(tup)

names = ["Fred", "Jim", "Sheila"]
print(names)
print(type(names))
print(names[0])
names[1] = "James"
print(names)
print(len(names))
# names[3] = "Alice"  # NOPE, out of range
names.append("Alice")
print(names)
names.sort(reverse=True)
print(names)
print(len(names))

numbers = range(0, 10)  # lazy ...
numbers = list(numbers)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

# slicing -- can add to your own data-types using "dunder" methods
print(numbers[2:6])  # not including the "fence"
print(numbers[2:6:2])  # stride size = 2
print(numbers[::-1])
print(numbers)  # slicing-access operations do not change the original list.

numbers[2:4] = [-1, -2, -3, -4, -5]  # but assignment slicing does :)
print(numbers)
