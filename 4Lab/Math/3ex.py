import math

n = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))

area = (n * length**2) / (4 * math.tan(math.pi/n))

print(f"The area of the regular polygon is {area:.2f}")