import pandas as pd
import random

def pick_word(words: dict) -> str:
    return random.choice(words["French"])


def word_generator() ->str:
    with open("french_words.csv", "r" ) as data_file:
        french_words = pd.read_csv(data_file)
    return pick_word(french_words)
