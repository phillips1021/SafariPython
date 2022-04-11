names = {"Fred": "Jones", "Alan": "Smith"}
print(names)
print(type(names))
print(names["Fred"])
print("Fred" in names)   # in searches in the *keys* of the dictionary
print("Jones" in names)  # False, jones is a *value*
print("Jones" in names.values())  # True

print(names.get("Albert"))  # None is a "singleton" value representing null/undefined
# print(names["Albert"])

names["Alfred"] = None
print("Alfred" in names)
print(names["Alfred"])

# comparison with Set

vowels = { "a", "e", "i" }
vowels.add("o")
vowels.add("u")
print(vowels)
print(type(vowels))

emptyset = set()
print(emptyset)
print(type(emptyset))

what = {}
print(type(what))

