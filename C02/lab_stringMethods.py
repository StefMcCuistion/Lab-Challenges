txt = "My precious!"
print(txt)
print(f".upper(): {txt.upper()}")
print(f".lower(): {txt.lower()}")
print(f"'PRECIOUS'.isupper(): {'PRECIOUS'.isupper()}")
print(f"'PRECIOUS'.islower(): {'PRECIOUS'.islower()}\n")

txt = "Who knows? Have patience. Go where you must go, and hope!"
print(txt)
print(f".capitalize(): {txt.capitalize()}")
print(f".title(): {txt.title()}\n")

txt = "1954"
print(f"'{txt}'.isnumeric(): {txt.isnumeric()}\n"
      f"'{txt}'.isalpha(): {txt.isalpha()}\n"
      f"'{txt}'.isalnum(): {txt.isalnum()}\n")

txt = "LOTR"
print(f"'{txt}'.isnumeric(): {txt.isnumeric()}\n"
      f"'{txt}'.isalpha(): {txt.isalpha()}\n"
      f"'{txt}'.isalnum(): {txt.isalnum()}\n")

txt = "LOTR1954"
print(f"'{txt}'.isnumeric(): {txt.isnumeric()}\n"
      f"'{txt}'.isalpha(): {txt.isalpha()}\n"
      f"'{txt}'.isalnum(): {txt.isalnum()}\n")

txt = "Your time will come. You will face the same Evil, and you will defeat \
it."
print(txt)
print(f".count('r'): {txt.count('r')}")
print(f".count('will'): {txt.count('will')}")
print(f".startswith('Your time'): {txt.startswith('Your time')}")
print(f".endswith('it.'): {txt.endswith('it.')}\n")

txt = ("It’s a dangerous business, Frodo, going out your door. You step onto "
       "the road, and if you don’t keep your feet, there’s no knowing where "
       "you might be swept off to.")
print(txt)
result = txt.replace('your', 'thy').replace('you', 'thou')
print(f"{result}\n")

txt = "Go where you must go, and hope!"
print(txt.split())
print("_".join(txt.split()) + "\n")

txt = "   Fly, you fools!   "
print(f"\"{txt}\"")
print(f".strip(): \"{txt.strip()}\"")
print(f".lstrip(): \"{txt.lstrip()}\"")
print(f".rstrip(): \"{txt.rstrip()}\"")
txt = "--++ Fly, you fools! ##,,"
print(f"\"{txt}\"")
print(f".strip(',-+# '): \"{txt.strip(',-+# ')}\"")


# Predict what the code does in comments below.
# HINT: Feel free to read up the docs for clues.
# https://docs.python.org/3/library/stdtypes.html#textseq
# BONUS: Attribute the quotes to the correct LOTR characters.
