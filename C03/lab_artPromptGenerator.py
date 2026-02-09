import random

# When artists are trying to keep a daily or regular art practice or
# challenge, it is hard to start from a blank canvas.

# We are often more creative when provided with art prompts.

# Write a art prompt generator for artists.
# The tool will generate 3 prompts for the user each time it's run.

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
    "District Attorney General",
    "Lord Commander",
    "Captain",
    "Philosopher-King",
    "Philosopher-Queen",
    "Warrior-King",
    "Warrior-Queen",
    "Pope",
    "Warrior-Pope",
    "Scholar-King",
    "Scholar-Queen",
    "Emperor",
    "Empress",
    "knight",
    "warrior",
    "maid",
    "droid",
    "fairy",
    "dragon"
]

prompt_jobs = [
    "woodworking",
    "gardening",
    "carpentry",
    "paperwork",
    "pencilpushing",
    "journalism",
    "research"
]

prompt_places = [
    "cemetary",
    "castle",
    "meadow",
    "forest",
    "glade",
    "wasteland",
    "abyss",
    "cave",
    "crypt",
    "maze",
    "dormitory",
    "hospital",
    "bank"
]

prompt_emotions = [
    'anger',
    'disgust',
    'sorrow',
    'regret',
    'lovesickness',
    'joy',
    'ecstasy',
    'delight',
    'whimsy'
]

prompt_lists = [prompt_plants, prompt_adjectives,
                prompt_titles, prompt_places, prompt_emotions,
                prompt_jobs]


def main():
    prompt_count = 3
    generate_prompt(prompt_lists, prompt_count)


def generate_prompt(prompt_lists, prompt_count):
    while prompt_count != 0:
        vowels = ['a', 'e', 'i', 'o', 'u']
        plant = random.choice(prompt_lists[0])
        if plant[0].lower() in vowels:
            plant_article = 'an'
        else:
            plant_article = 'a'
        adj = random.choice(prompt_lists[1])
        if adj[0].lower() in vowels:
            adj_article = 'an'
        else:
            adj_article = 'a'
        title = random.choice(prompt_lists[2])
        if title[0].lower() in vowels:
            title_article = 'an'
        else:
            title_article = 'a'
        place = random.choice(prompt_lists[3])
        emotion = random.choice(prompt_lists[4])
        job = random.choice(prompt_lists[5])
        prompt_templates = [
            f'{plant_article.title()} {plant} grows in {adj_article} {adj}'
            f' {place}, and it sparks {emotion}'
            f' in the {title}.',
            f'A once famous {title} hides in an abandoned {place},'
            f' practicing humble {job} with lingering {emotion}.',
            f'{job.title()} is now forbidden because of'
            f' the actions of one {title}.',
            f'{title_article.title()} {title} is on the run'
            f' after {emotion} is outlawed.',
            f'{adj_article.title()} {adj} {plant} becomes {title_article}'
            f' {title} because of a spell.',
            f'The {title} that rules over the {place} is filled with'
            f' {emotion} by the {adj} newcomer.',
            f'{title_article.title()} {adj} {title} will make you a master '
            f'of {job} if you trade away your {emotion}.',
            f'The {title} adventured into the {adj} {place} and returned '
            f'with the secret of {job}.'
            ]
        template = random.choice(prompt_templates)
        print(template)
        prompt_count -= 1


main()
