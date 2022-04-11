names = {"Fred": "Jones"}
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