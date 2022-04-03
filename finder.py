import json
file_a = json.load(open('prize.json'))['prizes']

import pandas as pd

df = pd.DataFrame.from_dict(file_a)

df = df.drop(columns=['overallMotivation'])
df = df.dropna().reset_index()

laureates = pd.json_normalize(df['laureates'])

laureates0 = pd.json_normalize(laureates[0])
laureates1= pd.json_normalize(laureates[1])
laureates2 = pd.json_normalize(laureates[2])

df = df.drop(columns=['laureates'])

df = df.merge(laureates0, left_index=True, right_index=True)
df = df.merge(laureates1, left_index=True, right_index=True)
df = df.merge(laureates2, left_index=True, right_index=True)

df.fillna('', inplace=True)

def find_place(df, searchplace, name):
    findname = df[df[f'{searchplace}'].str.contains(name)]
    findname_x = df[df[f'{searchplace}_x'].str.contains(name)]
    findname_y = df[df[f'{searchplace}_y'].str.contains(name)]
    return findname['id'].tolist(), findname_x['id_x'].tolist(), findname_y['id_y'].tolist()