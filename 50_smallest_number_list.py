numbers = [30,10,-45, 5,30]

minimum = numbers[0]
for n in numbers:
    if n < minimum:
        minimum = n
print(minimum)

print("The smallest number in the list is:", minimum)


