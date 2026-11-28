# write a python program that converts kilomenters to miles.

kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor : 
conversion_factor = 0.621371

miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles.")


def is_disarium(num):
    num_str = str(num)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return num == digit_sum

disarium_numbers = [num for num in range(1, 101) if is_disarium(num)]                                                                                                                 

print("Disarium numbers between 1 and 100:")
for num in disarium_numbers:
    print(num, end=" | ")

                                                                                                