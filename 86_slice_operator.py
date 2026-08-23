# Different ways to clone/copy a list in Python

# 1. Using Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print("Slice copy:", cloned_list)

# 2. Using list() constructor
cloned_list = list(original_list)
print("list() copy:", cloned_list)

# 3. Using List Comprehension
cloned_list = [item for item in original_list]
print("List comprehension copy:", cloned_list)

# 4. Using copy() method
cloned_list = original_list.copy()
print("copy() method:", cloned_list)

# 5. Using deepcopy for nested lists
import copy
nested_list = [[1, 2], [3, 4]]
deep_cloned_list = copy.deepcopy(nested_list)
print("Deep copy:", deep_cloned_list)

# Proof of difference between shallow and deep copy
shallow_copy = nested_list[:]
nested_list[0][0] = 99
print("After modifying original:")
print("Original:", nested_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_cloned_list)

