def divisible_by_5_and_7(n):
    # Generator function to yield numbers divisible by both 5 and 7
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

try:
    # Take input from user
    n = int(input("Enter a value for n: "))
    
    # Use generator and print result in comma-separated form
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")

