def triangle(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

# Examples
print(triangle(1))    # ➞ 1
print(triangle(6))    # ➞ 21
print(triangle(215))  # ➞ 23220


