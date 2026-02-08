print(2*3)  # 6
print(2-3)  # -1
print(1 + 2 / 3)  # 2 (2 / 3 is evaluated first. These are integers,
# so it'll round to 1. Then you get 1 + 1, which evaluates to 2.)
print((1 + 2) / 3)  # 1
print(1 - 0.1)  # 0.9 (performing an operation between an int and a
# float, Python will evaluate them both as floats)
print(0.1 + 0.1 + 0.1)  # 0.3
print(2**3)  # 8
print(8 % 3)  # 2 (8 over 3 = 2 with a remainder of 2)
print(type(0.1))  # float
print(type(2))  # integer
print(type("1.0"))  # string
print(int(1.1))  # 1
print(float(5))  # 5.0
print("3.3"*2)  # 3.33.3
print(float("3.3")*2)  # 6.6

# Predict what the code does using comments.

# Run the code to confirm your predictions.


# Investigate:

# What do you think caused the results of print(0.1 + 0.1 + 0.1)?

# What do you think the function type() does?

# In your own words, try to explain the results of print("3.3"*2) and
# print(float("3.3")*2)