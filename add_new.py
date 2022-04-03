import json
file_a = json.load(open('prize.json'))['prizes']

import pandas as pd

df1 = pd.DataFrame.from_dict(file_a)

laureates = pd.json_normalize(df1['laureates'])

laureates0 = pd.json_normalize(laureates[0])
laureates1= pd.json_normalize(laureates[1])
laureates2 = pd.json_normalize(laureates[2])

df1 = df1.drop(columns=['laureates'])

df1 = df1.merge(laureates0, left_index=True, right_index=True)
df1 = df1.merge(laureates1, left_index=True, right_index=True)
df1 = df1.merge(laureates2, left_index=True, right_index=True)

df1.fillna('', inplace=True)

def add_new(year, category, overallMotivation, id_x, firstname_x, surname_x, motivation_x, share_x, id_y, firstname_y, surname_y, motivation_y, share_y, id, firstname, surname, motivation, share):
    global df1
    df2 = pd.DataFrame({'year':[year],'category':category, 'overallMotivation':overallMotivation, 
    'id_x':id_x, 'firstname_x':firstname_x, 'surname_x':surname_x, 'motivation_x':motivation_x, 'share_x':share_x,
    'id_y':id_y, 'firstname_y':firstname_y, 'surname_y':surname_y, 'motivation_y':motivation_y, 'share_y':share_y,
    'id':id, 'firstname':firstname, 'surname':surname, 'motivation':motivation, 'share':share})
    df1 = pd.concat([df1, df2], ignore_index = True, axis = 0)
    return df1