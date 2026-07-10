# Sample List of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the largest value, set to the first element
largest = numbers[0]

# Iterate through the list and update the largest value if a bigger number is found
for i in numbers:
    if i > largest:
        largest = i

# Print the largest value
print("The largest number in the list is:", largest)


