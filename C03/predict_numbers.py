print(2*3)  # 6
print(2-3)  # -1
print(1 + 2 / 3)  # original answer was 2 because I assumed an integer
# divided by another integer would produce an integer, rounding to the nearest
# whole number. So, in my head it was (1 + 2 / 3) → (1 + 1) → 2
# but it's actually 1.666666... because the output of 2 / 3 is a float
print((1 + 2) / 3)  # original answer was 1 for the same reason as my previous
# wrong answer; I thought the result would be an integer. Actual answer is 1.0
# bc the output of (3 / 3) is a float. I don't understand why, though.
print(1 - 0.1)  # 0.9 (performing an operation between an int and a
# float, Python will evaluate them both as floats)
print(0.1 + 0.1 + 0.1)  # original answer was 0.3
# actual answer is specifically 0.30000000000000004 bc of innaccuracies in
# calculating with floats.
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