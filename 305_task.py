# Program 69: Merge Two Dictionaries

# 1. Using update() method (modifies dict1)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("Merged Dictionary (using update()):", dict1)

# 2. Using dictionary unpacking (creates new dict)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (using unpacking):", merged_dict)

# 3. Using | operator (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2
print("Merged Dictionary (using | operator):", merged_dict)

# 4. Handling overlapping keys (dict2 overrides dict1)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 99, 'c': 3}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (with overlapping keys):", merged_dict)

