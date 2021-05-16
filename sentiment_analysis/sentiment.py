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

text = """
The silicon chip inside her head
Gets switched to overload.
And nobody's gonna go to school today,
She's going to make them stay at home.
And daddy doesn't understand it,
He always said she was as good as gold.
And he can see no reasons
'Cause there are no reasons
What reason do you need to be shown?

Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I want to shoot
The whole day down.


The telex machine is kept so clean
As it types to a waiting world.
And mother feels so shocked,
Father's world is rocked,
And their thoughts turn to
Their own little girl.
Sweet 16 ain't so peachy keen,
No, it ain't so neat to admit defeat.
They can see no reasons
'Cause there are no reasons

What reason do you need?
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I want to shoot
The whole day down, down, down.

Shoot it all down


All the playing's stopped in the playground now
She wants to play with her toys a while.
And school's out early and soon we'll be learning
And the lesson today is how to die.
And then the bullhorn crackles,
And the captain tackles,
With the problems and the how's and why's.
And he can see no reasons
'Cause there are no reasons
What reason do you need to die?

The silicon chip inside her head
Gets switched to overload.
And nobody's gonna go to school today,
She's going to make them stay at home.
And daddy doesn't understand it,
He always said she was as good as gold.
And he can see no reasons
'Cause there are no reasons
What reason do you need to be shown?

Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like, I don't like
Tell me why?
I don't like Mondays.
Tell me why?
I don't like, I don't like
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I wanna shoot,
The whole day down.
"""

song_text = word_corpus_cleaning(text)

emotion_values = []
emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
y = 0

emotion_dict = {
    "Happy": read_pickle("happy"),
    "Angry": read_pickle("angry"),
    "Surprise": read_pickle("surprise"),
    "Sad": read_pickle("sad"),
    "Fear": read_pickle("fear")
}

for word in song_text:

    for emotion in emotion_dict.keys():

        if word in emotion_dict[emotion]:

            emotions[emotion] += 1

if sum(emotions.values()) is 0:
    print(emotions)
for i in emotions:
    emotion_values.append(round((emotions[i] / sum(emotions.values())), 2))
for j in emotions:
    emotions[j] = emotion_values[y]
    y += 1
print(emotions)