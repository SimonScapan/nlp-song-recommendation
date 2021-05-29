from sentiment_functions import *
import pickle

import spacy

nlp = spacy.load("en_core_web_lg")

def calc_emotions_per_song(song_text):

    song_text = word_corpus_cleaning(song_text, nlp)

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

    # iterate over song text
    for word in song_text:

        # check for every unique emotion
        for emotion in emotion_dict.keys():

            # if word is im emotion ditionary raise count by 1
            if word in emotion_dict[emotion]:

                emotions[emotion] += 1

    for i in emotions:
        
        emotion_values.append(round((emotions[i] / sum(emotions.values())), 2))

    for j in emotions:

        emotions[j] = emotion_values[y]
        y += 1

    return emotions
    
def calc_emotions_database(dataframe):

    # append new columns and set 0
    dataframe["Happy"] = 0
    dataframe["Angry"] = 0
    dataframe["Surprise"] = 0
    dataframe["Sad"] = 0
    dataframe["Fear"] = 0

    start = 0

    # create list of songs where no emotion could be calculated
    no_emotion_list = []
    errors = 0
    for i in range(len(dataframe)):

        try: 

            emotions = calc_emotions_per_song(dataframe.loc[i, "Song_text"])
        
        except: 

            print("Error: ", errors)
            errors += 1
            emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
            no_emotion_list.append(dataframe.loc[i, "Song_title"])

        # add emotions column to dataframe
        dataframe.loc[i, "Happy"] = emotions["Happy"]
        dataframe.loc[i, "Angry"] = emotions["Angry"]
        dataframe.loc[i, "Surprise"] = emotions["Surprise"]
        dataframe.loc[i, "Sad"] = emotions["Sad"]
        dataframe.loc[i, "Fear"] = emotions["Fear"]

        if start % 50 == 0:

            print("iter: ", start)
        
        start += 1
    
    # save not calulatable song titles
    save_as_pickle("not_calc_songs", no_emotion_list)

    # save dataframe
    with open("../data/musicdata_sentimented.pkl", "wb") as file:

        pickle.dump(dataframe, file, protocol=pickle.HIGHEST_PROTOCOL)

    # return dataframe

# read dataframe
# data = pd.read_pickle("../data/master_music_data.pkl")

# get emotions for whole dataframe and save it
# calc_emotions_database(data)

# check if everything workes
# data2 = pd.read_pickle("../data/musicdata_sentimented.pkl")
# print(data2[:2])
# print(data2["Angry"].head(100))

# append_to_pickle("happy", ["happiness"]) # happinies obviusoly not in dataset --> append with this funciton