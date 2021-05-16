from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import pickle
import re

# define function to import word_classifications

def save_as_pickle(filename, file):

    with open(f"{filename}.pkl", "wb") as save_file:

        pickle.dump(file, save_file, protocol=pickle.HIGHEST_PROTOCOL)

def read_pickle(filename):

    pickle_file = pd.read_pickle(f'{filename}.pkl')

    return pickle_file

def append_to_pickle(filename, data):

    pickle_file = pd.read_pickle(f"{filename}.pkl")

    pickle_file += data

    save_as_pickle(filename, pickle_file)

def clean_apostrophes(word):

    # check if cleaning nececary
    if "'" in word:
        
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

        return word

    else:

        return word

def clean_nonalpha(song_text):

    replace_list = [".", ",", "!", "?", "-", ";", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")"]

    for element in replace_list:

        song_text = song_text.replace(element, "")
    
    return song_text

def clean_shortcuts(word):

    # read shortcut dict from pickle file
    shortcuts = read_pickle("shortcuts")

    if word in shortcuts.keys():

        word = shortcuts[word]
    
    return word

def clean_negations(song_text):

    negations_dict = {}
    angry_tmp = read_pickle("angry_not")
    empty_tmp = read_pickle("empty_not")
    fear_tmp = read_pickle("fear_not")
    sad_tmp = read_pickle("sad_not")
    happy_tmp = read_pickle("happy_not")

    for entry in angry_tmp:

        negations_dict[entry] = "angry"

    for entry in empty_tmp:

        negations_dict[entry] = "empty"

    for entry in fear_tmp:

        negations_dict[entry] = "fear"

    for entry in sad_tmp:

        negations_dict[entry] = "sad"

    for entry in happy_tmp:

        negations_dict[entry] = "happy"

    negation_pairs = re.findall("not\s\w+", song_text)

    for pair in negation_pairs:

        try:

            song_text = song_text.replace(pair, negations_dict[pair])

        except:

            print("missing not pair in negation: ", pair)

            pass

    return song_text

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

    # clean up non alphanumerical signs
    song_text = clean_nonalpha(song_text)

    # clean up shortcuts
    song_text = " ".join([clean_shortcuts(word) for word in song_text.split(" ")])

    # clean up negations - here full text because of 2 word patterns
    song_text = clean_negations(song_text)

    # tokenize
    song_text = word_tokenize(song_text)

    # clean up stop words
    song_text_tmp = []
    for word in song_text:

        word = clean_stopwords(word)

        if word is not None:
            song_text_tmp.append(word)
    
    song_text = song_text_tmp
    song_text_tmp = None

    # lammetize song text
    song_text = [lemmatization(word) for word in song_text]

    # print(song_text)
    return song_text