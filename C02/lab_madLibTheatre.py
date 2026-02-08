# Write a The Tonight Show inspired Mad Lib Theatre program.
#
# Your program will prompt the user for between 4-6 silly nouns, verbs,
# adjectives, etc...
#
# Then it will make use of the words to display a series of lines from a
# dramatic script.
#
# You may choose to come up with your own lines or use lines from
# a movie involving 2 characters.
#
# Format the input to use appropriate grammer and cases. Also remove any
# extra white spaces in the input.
#
# Have fun!

number = input("Enter a number: ").title()
noun_singular_1 = input("Enter a singular noun (example: thing): ").title()
noun_singular_2 = input("Enter another singular noun: ").lower()
noun_singular_3 = input("Enter another singular noun: ").lower()
noun_plural_1 = input("Enter a plural noun (example: things): ").title()
noun_plural_2 = input("Enter another plural noun: ").lower()
verb_past_tense_1 = input("Enter a past tense verb (example: moved): ").lower()
verb_past_tense_2 = input("Enter another past tense verb: ").lower()
title_1 = input(
    "Enter a title a person might have (example: President): ").title()
title_2 = input("Enter another title: ").title()
name = input("Enter a name a person might have (example: John): ").title()

article = "a"
vowels = ["a", "e", "i", "o", "u"]
if title_2[0].lower() in vowels:
    article = "an"

line = (
    f"Long ago, the {number} {noun_plural_1} lived together in harmony.\n"
    f"Then everything changed when the {noun_singular_1} "
    f"{verb_past_tense_1}.\nOnly the {title_1}, master of all {number.lower()}"
    f" {noun_plural_2}, could stop them,\nbut when the world needed him most, "
    f"he {verb_past_tense_2}.\nA hundred years passed and my {noun_singular_2}"
    f" and I discovered the new {title_1}: {article} {title_2} named {name}."
)

print(line)
#
# See Mad Lib Theater with Benedict Cumberbatch and Jimmy Fallon.
# https://www.youtube.com/watch?v=kM9Wuzj4k24
