# Sample dictionary
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sort by Keys
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")

print()  # Line break

# Sort by Values
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")