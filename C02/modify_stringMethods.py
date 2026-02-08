noun = "Good"
place = "  World  "
person = "mr. frodo"
ing_verb = "fighting"
attribution = "-- Sam gamgee"
quote = (f"'There's some {noun.lower()} in this {place.lower().strip()}, \
{person.title()}… "
         f"and it's worth {ing_verb} for.'"
         f"\n- {attribution.title().strip('- ')}")
print(quote)
print(f"{noun},{place},{person},{ing_verb},{attribution}")


# Modify the code above, so that it displays as below:
# "There's some good in this world, Mr. Frodo… and it's worth fighting for."
# - Sam Gamgee
# Good,  World  ,mr. frodo,fight,-- Sam gamgee
#
# The quote is in the first line and the attribution in the second line.
# Use only string methods to accomplish this.
# The values of the original variables should remain unchanged.
# You may create new variables.
