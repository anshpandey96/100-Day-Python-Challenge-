# Write a program to print all prime Number in an interval of 1 -10

lower = 1 
upper = 10 

print("Print number between ", lower, "and",upper, "are:")

for num in range(lower , upper+1):
    # all prime number are greater than 1 

    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print(num)    

