import pandas as pd
import pickle
import re
import spacy

## DISCLAIMER: Code is based on text2emotion package, but improved by using spacy package and adding modular parts

def save_as_pickle(filename, file):

    with open(f"{filename}.pkl", "wb") as save_file:

        pickle.dump(file, save_file, protocol=pickle.HIGHEST_PROTOCOL)

def read_pickle(filename):

    pickle_file = pd.read_pickle(f'{filename}.pkl')

    return pickle_file

# give user the ability to append new word to saved pickle files
def append_to_pickle(filename, data):

    pickle_file = pd.read_pickle(f"{filename}.pkl")

    pickle_file += data

    save_as_pickle(filename, pickle_file)

def clean_apostrophes(word):

    # check if cleaning nececary
    if "'" in word:
        
        # define all apostrophes and shortcuts to resolve them
        word = re.sub("won't", "will not", word)
        word = re.sub("doesn't", "does not", word)
        word = re.sub("don't", "do not", word)
        word = re.sub("ain't", "am not", word)
        word = re.sub("won't", "will not", word)
        word = re.sub("i'll", "i will", word)
        word = re.sub("we'll", "we will", word)
        word = re.sub("i'm", "i am", word)
        word = re.sub("we're", "we are", word)
        word = re.sub("here's", "here is", word)
        word = re.sub("that's", "that is", word)
        word = re.sub("he's", "he is", word)
        word = re.sub("she's", "she is", word)
        word = re.sub("'cause", "because", word)
        word = re.sub("can't", "can not", word)
        word = re.sub("n't", "not", word)
        word = re.sub("c'mon", "come on", word)

        return word

    else:

        return word

def remove_word_types(song_text, nlp):
    "remove Punctuation, Spaces, etc."
    
    # create list for clean words
    clean_text = []
    
    # iterate over song text
    for token in song_text:
        
        # get pos of token
        token_pos = token.pos_
        
        # check if pos has to be excluded | AUX = auxiliary verb, SCONJ =  subordinating conjunction
        if token_pos not in ["SPACE", "PUNCT", "NUM", "SYM", "PRON", "AUX", "SCONJ"]:
            
            clean_text.append(token.text)
        
        else:
            
            pass
    
    return nlp(" ".join(clean_text))

def remove_entities(song_text, nlp):
    
    clean_text = []
    
    # get all entities from song text
    entities = [entity.text for entity in song_text.ents]
    
    for token in song_text:
        
        # check if token is not an entity
        if token.text not in entities:
            
            clean_text.append(token.text)
            
    return nlp(" ".join(clean_text))

def clean_shortcuts(word):

    # read shortcut dict from pickle file
    shortcuts = read_pickle("shortcuts")

    if word in shortcuts.keys():

        word = shortcuts[word]
    
    return word

def clean_negations(song_text):

    negations_dict = {}
    angry = read_pickle("angry_not")
    empty = read_pickle("empty_not")
    fear = read_pickle("fear_not")
    sad = read_pickle("sad_not")
    happy = read_pickle("happy_not")

    not_included = []

    for entry in angry:

        negations_dict[entry] = "angry"

    for entry in empty:

        negations_dict[entry] = "empty"

    for entry in fear:

        negations_dict[entry] = "fear"

    for entry in sad:

        negations_dict[entry] = "sad"

    for entry in happy:

        negations_dict[entry] = "happy"

    negation_pairs = re.findall("not\s\w+", song_text)

    for pair in negation_pairs:

        try:

            song_text = song_text.replace(pair, negations_dict[pair])

        except:

            not_included.append(pair)
    
    # save not included negations
    append_to_pickle("missing_negations", not_included)

    return song_text

def clean_stopwords(song_text, nlp):

    # load english stopwords from spacy
    stop_words = nlp.Defaults.stop_words
    
    # create word list without stopwords
    clean_text = [word for word in song_text if not word in stop_words]
    
    return nlp(" ".join(clean_text))
    

def lemmatization(song_text):

    # iterate over song text and lemmatize every word
    song_text_lemma = [token.lemma_ for token in song_text]

    return song_text_lemma

def word_corpus_cleaning(song_text, nlp):

    # lower text
    song_text = song_text.lower()

    # clean up apostrophes
    song_text = " ".join([clean_apostrophes(word) for word in song_text.split(" ")])
    
    # clean up shortcuts
    song_text = " ".join([clean_shortcuts(word) for word in song_text.split(" ")])
    
    # clean up negations - here full text because of 2 word patterns - afterwards convert to nlp object
    song_text = nlp(clean_negations(song_text))

    # clean up text from punctuation, non alpha elements, pronouns, etc.
    song_text = remove_word_types(song_text, nlp)
    
    # clean up entities (like countries, organisations, etc.)
    song_text = remove_entities(song_text, nlp)

    # tokenize text
    song_text = [token.text for token in song_text]

    # clean up stop words
    song_text = clean_stopwords(song_text, nlp)

    # lammetize song text
    song_text = lemmatization(song_text)

    # print(song_text)
    return song_text