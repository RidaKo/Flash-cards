import pandas as pd
import random


def word_generator() ->dict:
    """
    ## Word generator

    Returns a dictionary of a french word and an english translation
    
    - Use the key **French** to acces french words and **English** to access english words

    """
    with open("french_words.csv", "r" ) as data_file:
        words = pd.read_csv(data_file)
    random_df_word_row = words.iloc[random.randint(1,100)]
    return {"French": random_df_word_row["French"],  "English":random_df_word_row["English"]}
