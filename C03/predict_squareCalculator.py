print("Square Calculator")
length = input("Enter the length of the sides in meters: ")
length = float(length)  # converts string input to float
area = length * length  # area of square with side length = {length}
perimeter = length * 4  # perimeter of square with side length = {length}
print(f"The area is {round(area, 4)} m^2")  # rounds to four digits
# I'd originally guessed that it would round to the nearest multiple of four
print(f"The perimeter is {perimeter} m")

# Predict what the code does using comments.

# Run the code to confirm your predictions.

# Investigate:

# Why does the code use float() on line 3?

# Answer: if you don't convert the string to a numeric datatype, you can't
# multiply it by itself.
