my_list = [1, 2, 3, 4]
print(my_list)

print(my_list[2])

print(my_list[:2])

my_list.append(5)
print(my_list)

del my_list[0]
print(my_list)

print(my_list.pop())
print(my_list)

my_list = my_list + [6, 7, 8]
print(my_list)

my_list.insert(3, 5)
print(my_list)

my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)

my_list = ['a', 'b', 'c', 'b']
print(my_list.count('b'))
print(my_list.index('b'))

my_other_list = my_list.copy()
print(my_list)
print(my_other_list)


# Predict what the code does using comments.

# Run the code to confirm your predictions.