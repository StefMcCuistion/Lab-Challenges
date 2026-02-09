my_list = [1, 2, 3, 4]
print(my_list)  # Prediction: [1, 2, 3, 4]

print(my_list[2])  # Prediction: 3

print(my_list[:2])  # Prediction: 1, 2
# Correction: forgot to put brackets around output to indicicate it's a list. Should be [1, 2]

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
# Correction: should be [2, 3, 4, 5, 6, 7, 8].
# I assumed .insert() would insert an item after appearances of its first parameter in the list. 
# So I thought 5 would appear after the appearance of 3, rather than at index 3. 

my_list.clear()
print(my_list)  # Prediction: []

my_list = ['a', 'b', 'c', 'b']
print(my_list.count('b'))  # Prediction: 2
print(my_list.index('b'))  # Prediction: [1, 3]
# Correction: 1
# .index() returned the index of "b"'s first appearance, rather than a list of 
# all indices where "b" is found. 

my_other_list = my_list.copy()
print(my_list)  # Prediction: ['a', 'b', 'c', 'b']
print(my_other_list)  # Prediction: ['a', 'b', 'c', 'b']


# Predict what the code does using comments.

# Run the code to confirm your predictions.