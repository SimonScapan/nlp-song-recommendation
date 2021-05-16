from sentiment_functions import *

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

import text2emotion as te

def calc_emotions_per_song(song_text):

    emotions = te.get_emotion(text)

    return emotions

def calc_emotions_per_song_man(song_text):

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

    for i in range(len(dataframe)):

        emotions = calc_emotions_per_song(dataframe.loc[i, "Lyrics"])

        # add emotions column to dataframe
        dataframe.loc[i, "Happy"] = emotions["Happy"]
        dataframe.loc[i, "Angry"] = emotions["Angry"]
        dataframe.loc[i, "Surprise"] = emotions["Surprise"]
        dataframe.loc[i, "Sad"] = emotions["Sad"]
        dataframe.loc[i, "Fear"] = emotions["Fear"]
    
    return dataframe

# import pandas as pd
# a = pd.DataFrame({"Lyrics":[text]})

# b = calc_emotions_database(a)
# print(b.values)

print(calc_emotions_per_song_man(text))