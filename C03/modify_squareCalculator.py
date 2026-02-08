print("Square Calculator")
length = input("Enter the length of the rectangle in meters: ")
width = input("Enter the width of the rectangle in meters: ")
length = float(length)
width = float(width)
area = length * width
perimeter = (length * 2) + (width * 2)
print(f"The area is {round(area, 2)} m^2")
print(f"The perimeter is {round(perimeter, 2)} m")

# Modify the above code to:

# 1. Work for a rectangle, by also asking the user for the width.

# 2. Display numbers for area and perimeter so they are rounded to the
# nearest 2 digits after the decimal point.
# view rawpyfda_c03_05.py hosted with ❤ by GitHub
