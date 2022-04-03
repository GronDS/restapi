import json
file_a = json.load(open('prize.json'))['prizes']

import pandas as pd
df_c = pd.DataFrame.from_dict(file_a)

df_c = df_c.drop(columns=['overallMotivation'])
df_c = df_c.dropna().reset_index()

def pop_cats(df_c):
  df_c = df_c.groupby(['category'])['category'].count().reset_index(
  name='Count').sort_values(['Count'], ascending=False)
  return df_c[0:5].to_json(orient='split')