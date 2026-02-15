import random


houses = ['Griffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
characters = ['Elsa', 'Anna', 'Olaf', 'Moana', 'Snow White']
my_house = random.choice(houses)
my_character = random.choice(characters)

print(f"Sorting Hat: {my_character}, you will be sent to {my_house.upper()}!")

# Modify the code above so the sorting hat, sorts a randomly picked
# Disney character into a house in Hogwarts.