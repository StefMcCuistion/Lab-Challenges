my_list = [1, 2, 3, 4]
print(my_list)  # Prediction: [1, 2, 3, 4]

print(my_list[2])  # Prediction: 3

print(my_list[:2])  # Prediction: 1, 2

my_list.append(5)
print(my_list)  # Prediction: [1, 2, 3, 4, 5]

del my_list[0]
print(my_list)  # Prediction: [2, 3, 4, 5]

print(my_list.pop())  # Prediction: 5
print(my_list)  # Prediction [2, 3, 4]

my_list = my_list + [6, 7, 8]
print(my_list)  # Prediction: [2, 3, 4, 6, 7, 8]

my_list.insert(3, 5)
print(my_list)  # Prediction: [2, 3, 5, 4, 6, 7, 8]

my_list.reverse()
print(my_list)  # Prediction: [8, 7, 6, 4, 5, 3, 2]

my_list.clear()
print(my_list)  # Prediction: []

my_list = ['a', 'b', 'c', 'b']
print(my_list.count('b'))  # Prediction: 2
print(my_list.index('b'))  # Prediction: [1, 3]

my_other_list = my_list.copy()
print(my_list)  # Prediction: ['a', 'b', 'c', 'b']
print(my_other_list)  # Prediction: ['a', 'b', 'c', 'b']


# Predict what the code does using comments.

# Run the code to confirm your predictions.