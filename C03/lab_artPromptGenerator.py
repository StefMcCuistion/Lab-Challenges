import random

# When artists are trying to keep a daily or regular art practice or
# challenge, it is hard to start from a blank canvas.
#
# We are often more creative when provided with art prompts.
#
# Write a art prompt generator for artists.
# The tool will generate 3 prompts for the user each time it's run.

prompt_templates = [
    f'A {plant} grows in a {adj} {place}, and it sparks {emotion} in the {title}.',
    f'A once famous {title} hides in an abandoned {place},'
    f'practicing humble {job} with lingering {emotion}.',
    f'{job.title()} is forbidden because of the actions of one {title}.'
]

prompt_plants = [
    "tree",
    "sapling",
    "bush"
]

prompt_adjectives = [
    "tiresome", 
    "foreboding", 
    "ominous", 
    "majestic",
    "wondrous",
    "fantastic",
    "gloomy",
    "sunny",
    "hot",
    "icy",
    "wintry",
    "industrial",
    "grand"
]

prompt_titles = [
    "King",
    "Queen",
    "Judge",
    "Lord",
    "Lawyer",
    "Attorney",
    "Chancellor",
    "Adjudicator",
    "District General",
    "Lord Commander",
    "Captain",
    "Philosopher-King",
    "knight",
    "warrior",
    "maid",
    "droid"
]

prompt_jobs = [
    "woodworking",
    "gardening",
    "carpentry",
    "clerical work",
    "pencilpushing",
    "journalism"
]

def main(): 
    print(generate_prompt())
    print(generate_prompt())
    print(generate_prompt())

def generate_prompt(): 
    return

main()