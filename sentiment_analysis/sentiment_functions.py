from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import re

# define function to import word_classifications
def read_pickle(filename):

    pickle_file = pd.read_pickle(f'{filename}.pickle')

    return pickle_file

def clean_apostrophes(word):

    # check if cleaning nececary
    if "'" in word:
        
        word = re.sub("won't", "will not", word)
        word = re.sub("don't", "do not", word)
        word = re.sub("n't", "not", word)
        word = re.sub("won't", "will not", word)
        word = re.sub("i'll", "i will", word)
        word = re.sub("i'm", "i am", word)
        word = re.sub("we're", "we are", word)
        word = re.sub("here's", "here is", word)
        word = re.sub("that's", "that is", word)
        word = re.sub("he's", "he is", word)
        word = re.sub("she's", "she is", word)

        return word

    else:

        return word

def clean_shortcuts(word):

    # read shortcut dict from pickle file
    shortcuts = read_pickle("shortcuts")

    if word in shortcuts.keys():

        word = shortcuts[word]
    
    return word

def clean_stopwords(word):

    # load english sstopwords from nltk
    stop_words = set(stopwords.words('english'))
    
    # return if word is not a stop word
    if word in stop_words:

        pass

    else:

        return word

def lemmatization(word):

    # load nltk lemmatizer
    lemma = WordNetLemmatizer()
    word = lemma.lemmatize(word, 'v')
    word = lemma.lemmatize(word, 'n')

    return word

def word_corpus_cleaning(song_text):

    # lower text
    song_text = song_text.lower()

    # clean up spaces (set max amount of spaces found in lyrics)
    for i in range(2,5):
        
        song_text = song_text.replace(i*" ", " ")

    # clean up apostrophes
    song_text = " ".join([clean_apostrophes(word) for word in song_text.split(" ")])

    # clean up shortcuts
    song_text = " ".join([clean_shortcuts(word) for word in song_text.split(" ")])

    # remove digits and other non alpha parts
    song_text = " ".join([i for i in song_text.split(" ") if  i.isalpha()])

    # remove 

    # tokenize
    song_text = " ".join(word_tokenize(song_text))
    

    # clean up stop words
    song_text_tmp = []
    for word in song_text.split(" "):

        word = clean_stopwords(word)

        if word is not None:
            song_text_tmp.append(word)
    
    song_text = " ".join(song_text_tmp)
    song_text_tmp = None

    # lammetize song text
    song_text = " ".join([lemmatization(word) for word in song_text.split(" ")])

    # print(song_text)
    return song_text