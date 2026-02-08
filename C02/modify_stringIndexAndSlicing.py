quote = '"Not all those who wander are lost." - Bilbo Baggins'
print(quote)
length = len(quote)
print(
      f"Total characters: {length}\n"
      f"First character: {quote[0]}\n"
      f"6th character: {quote[5]}\n"
      f"Index of first 'o': {quote.find('o')}\n"
      f"Index of last 'o': {quote.rfind('o')}\n"
      f"Last character: {quote[length-1]}\n"
      f"2nd last character: {quote[-2]}\n"
      f"Characters from index 5 to 8 (excl. 8): {quote[5:8]}\n"
      f"Characters from index 0 to 6 (excl. 6): {quote[:6]}\n"
      f"Characters from index 5 to the end: {quote[5:]}"
      f"The word 'Baggins': {quote[-7:]}\n"
      f"The word 'Not': {quote[1:4]}\n"
      f"The word 'wander': {
          quote[quote.find('wander'):(quote.find('wander')+6)]}"
      )
new_quote = quote[:(quote.find('-'))] + "-" + quote[quote.find('-'):]
print(new_quote)


# - Fix any errors in the code first.
# - Modify the code to also display the words 'Baggins', '"Not' and
# 'wander'.
# - Using the .find() method and string concatenation, find the '-' in
# the quote and relace it with '--'.
