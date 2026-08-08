class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num


# Example usage:
n = int(input("Enter the range limit: "))
generator = DivisibleBySeven(n).generate_divisible_by_seven()

print("Numbers divisible by 7 between 0 and", n, ":")
for number in generator:
    print(number)

