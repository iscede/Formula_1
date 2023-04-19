# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:20:53 2023

@author: andre
"""
#\N
import pandas as pd

df = pd.read_csv("merge_data.csv")

df = df.apply(lambda x: x.replace('\\N', '0'))

df['position'] = pd.to_numeric(df['position'])

df = df[['grid', 'position', 'forename', 'surname', 'name', 'constructorName']]
df = df.rename(columns = {"name":"circuitName"})

