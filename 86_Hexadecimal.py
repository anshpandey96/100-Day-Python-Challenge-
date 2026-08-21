import math

def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return round(area, 1)

# Example usage:
print(area_of_hexagon(1))  # Output: 2.6
print(area_of_hexagon(2))  # Output: 10.4
print(area_of_hexagon(3))  # Output: 23.4



