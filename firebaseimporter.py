import pandas as pd
import requests
data = pd.read_pickle("../master_music_data.pkl")
data.dropna()
data = data.fillna(0)
data.columns = map(str.lower, data.columns)

counter=0
for index, row in data.iterrows():
    row_dict = row.to_dict()
    response_status = requests.post(url="https://murat-db-20-default-rtdb.firebaseio.com/.json", json=row_dict)
    
    if response_status.status_code != 200:
        print(response_status)
    if counter % 20 == 0:
        print(counter)
    counter += 1