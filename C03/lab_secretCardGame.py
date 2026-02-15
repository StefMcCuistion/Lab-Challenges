import random

cards = ['ace', 'king', 'queen', 'jack']
secret_card = random.choice(cards)
prizes = ['a cookie', 'a gold star', 'a chocolate-covered strawberry', 
          'the secret of life', 'a map to the fountain of youth', 
          'a candy bar', 'a shiny coin', 'a gold bar']
guess = input("What is the secret card? ")
guess = guess.strip().lower()
print(f'You guessed {guess}.')
if secret_card == guess:
    print(f"You win! The secret card was a {secret_card}!")
    prize = random.choice(prizes)
    print(f"You get {prize}!")
else:
    print(f"Too bad! The correct answer was {secret_card}!")
