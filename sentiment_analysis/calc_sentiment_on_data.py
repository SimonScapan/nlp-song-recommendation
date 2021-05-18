from sentiment_functions import *
import pickle

# text = """
# The silicon chip inside her head
# Gets switched to overload.
# And nobody's gonna go to school today,
# She's going to make them stay at home.
# And daddy doesn't understand it,
# He always said she was as good as gold.
# And he can see no reasons
# 'Cause there are no reasons
# What reason do you need to be shown?

# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# I want to shoot
# The whole day down.


# The telex machine is kept so clean
# As it types to a waiting world.
# And mother feels so shocked,
# Father's world is rocked,
# And their thoughts turn to
# Their own little girl.
# Sweet 16 ain't so peachy keen,
# No, it ain't so neat to admit defeat.
# They can see no reasons
# 'Cause there are no reasons

# What reason do you need?
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# I want to shoot
# The whole day down, down, down.

# Shoot it all down


# All the playing's stopped in the playground now
# She wants to play with her toys a while.
# And school's out early and soon we'll be learning
# And the lesson today is how to die.
# And then the bullhorn crackles,
# And the captain tackles,
# With the problems and the how's and why's.
# And he can see no reasons
# 'Cause there are no reasons
# What reason do you need to die?

# The silicon chip inside her head
# Gets switched to overload.
# And nobody's gonna go to school today,
# She's going to make them stay at home.
# And daddy doesn't understand it,
# He always said she was as good as gold.
# And he can see no reasons
# 'Cause there are no reasons
# What reason do you need to be shown?

# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like, I don't like
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like, I don't like
# Tell me why?
# I don't like Mondays.
# Tell me why?
# I don't like Mondays.
# I wanna shoot,
# The whole day down.
# """

text = """
It might seem crazy what I'm about to say
Sunshine she's here, you can take a break
I'm a hot air balloon that could go to space
With the air, like I don't care baby by the way

Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do

Here come bad news talking this and that
Yeah, well, gimme all you got and don't hold back
Yeah, well I should probably warn you I'll be just fine
Yeah, no offense to you don't waste your time
Here's why


Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do

(Happy) bring me down
Can't nothing (happy) bring me down
My level's too high (happy) to bring me down
Can't nothing (happy) bring me down
I said
(Happy, happy, happy) bring me down
Can't nothing bring me down
My level's too high (happy) to bring me down
Can't nothing bring me down
I said

Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do


Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do

(Happy) bring me down
Can't nothing (happy) bring me down
My level's too high (happy) to bring me down
Can't nothing (happy) bring me down
I said

Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do

Because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do

C'mon


"""

import text2emotion as te

def calc_emotions_per_song(song_text):

    emotions = te.get_emotion(text)

    return emotions

def calc_emotions_per_song_cust(song_text):

    song_text = word_corpus_cleaning(song_text)

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


    return emotions

def calc_emotions_database(dataframe):

    # append new columns and set 0
    dataframe["Happy"] = 0
    dataframe["Angry"] = 0
    dataframe["Surprise"] = 0
    dataframe["Sad"] = 0
    dataframe["Fear"] = 0

    start = 0

    for i in range(len(dataframe)):

        emotions = calc_emotions_per_song_cust(dataframe.loc[i, "Lyrics"])

        # add emotions column to dataframe
        dataframe.loc[i, "Happy"] = emotions["Happy"]
        dataframe.loc[i, "Angry"] = emotions["Angry"]
        dataframe.loc[i, "Surprise"] = emotions["Surprise"]
        dataframe.loc[i, "Sad"] = emotions["Sad"]
        dataframe.loc[i, "Fear"] = emotions["Fear"]

        if start % 500 == 0:

            print("iter: ", start)
        
        start += 1
    
    # save dataframe
    with open("../data/musicdata_tmp.pkl", "wb") as file:

        pickle.dump(dataframe, file, protocol=pickle.HIGHEST_PROTOCOL)

    # return dataframe

#data = pd.read_pickle("../data/musicdata.pkl")
#data = data[:1]
#print(data["Lyrics"])
# print("unique",len(data["Lyrics"].unique()))

#print("start len data:", len(data))
#data = data.dropna(subset=["Lyrics"])
#data = data.reset_index(drop = True)
#print("Data after null values: ", len(data))

#calc_emotions_database(data)
data2 = pd.read_pickle("../data/musicdata_tmp.pkl")
print(data2.head())

# import pandas as pd
# a = pd.DataFrame({"Lyrics":[text]})

# b = calc_emotions_database(a)
# print(b.head())

#print(calc_emotions_per_song(text)) # compaare to package
#print(calc_emotions_per_song_cust(text))

# append_to_pickle("happy", ["happy", "happiness"]) # happinies obviusoly not in dataset --> append with this funciton
# print(calc_emotions_per_song_cust(text))