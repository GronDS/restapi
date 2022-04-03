from typing import Dict
from fastapi import FastAPI
import pandas as pd
import json
from finder import df, find_place
from categories import df_c, pop_cats
from add_new import df1, add_new



app = FastAPI()

@app.get('/')
def home():
    return pop_cats(df_c)

@app.get('/sp/{sp}/name/{name}/')
def get_name_sp(sp: str=None, name: str=None):
    return find_place(df, sp, name)

@app.get('/actual')
def add_row(year: str='', category: str='', overallMotivation: str='',
id_x: str='', firstname_x: str='', surname_x: str='', motivation_x: str='', share_x: str='',
id_y: str='', firstname_y: str='', surname_y: str='', motivation_y: str='', share_y: str='',
id: str='', firstname: str='', surname: str='', motivation: str='', share: str=''):
    return add_new(year, category, overallMotivation, id_x, firstname_x, surname_x, motivation_x, share_x, id_y, firstname_y, surname_y, motivation_y, share_y, id, firstname, surname, motivation, share)
