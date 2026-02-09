import random

cards = ['ace', 'king', 'queen', 'jack']
secret_card = random.choice(cards)
guess = input("What is the secret card? ")
guess = guess.strip().lower()
print(f'You guessed {guess}.')
if secret_card == guess:
    print(f"You win! The secret card was a {secret_card}!")
else:
    print(f"Too bad! The correct answer was {secret_card}!")
