import pandas as pd
import random

class WordManager():
    """
        ## Word generator class
        Creates a word manager object
        The objects primary function is to manipulate words
    """
    def __init__(self) -> None:
        self.words_to_learn = self.read_words_from_file()
        self.word_pair = None
        

    def read_words_from_file(self) -> object:
        """
        Returns a DataFrame object that is filled with all words
        """
        try:
            data_file = open("data/words_to_learn.csv" ,"r")
            words = pd.read_csv(data_file)

        except(FileNotFoundError,pd.errors.EmptyDataError) as error:
            
            if error == pd.errors.EmptyDataError:
                print("You have learned all the words or the file has been corrupt.\n Starting over")
            elif error == FileNotFoundError:
                print("File with your records has not been found inserting default file.")

            data_file = open("data/french_words.csv" ,"r")
            words = pd.read_csv(data_file)
        finally:     
            data_file.close()
            return words
        
    
    def remove_words_and_write_to_learnt_file(self) ->None:
        with open("data/words_to_learn.csv", "w") as word_file:
            for word in self.words_to_learn["French"]:
                if word == self.word_pair["French"]:
                    # getting the index of the element based on the condition
                    index = self.words_to_learn.loc[self.words_to_learn["French"]==word].index.to_list()[0]
                    #print(index)
                    #print(self.words_to_learn.loc[self.words_to_learn["French"]==word])
                    self.words_to_learn = self.words_to_learn.drop(index)
                    print(self.words_to_learn)
                    self.words_to_learn.to_csv(word_file, index = False, lineterminator ='\n')
                
                
    def generate_words(self) ->None:
        """
        ## Word generator

        Creates a dictionary of a french word and an english translation and adds
        it as word_pair atribute
        
        - Use the key **French** to acces french words and **English** to access english words

        """
        rand_index_of_row = random.choice([number for number in self.words_to_learn.index.values.tolist()])
        #print(rand_num)
        random_df_word_row = self.words_to_learn.loc[rand_index_of_row]
        #print(random_df_word_row)
        self.word_pair = {"French": random_df_word_row["French"],  "English":random_df_word_row["English"]}

#random.choice([number for number in self.words_to_learn.index.values.tolist()