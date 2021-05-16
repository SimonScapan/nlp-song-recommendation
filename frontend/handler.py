import pandas as pd

col_names =  ['Title', 'Interpret', 'Genre', 'Lyrics', 'Happy', 'Angry', 'Surprise', 'Sad', 'Fear']

df  = pd.DataFrame(columns = col_names)
df.to_pickle('./../data/musicdata.pkl')