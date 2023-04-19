# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:20:40 2023

@author: andre
"""

#https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

results = pd.read_csv("results.csv")
circuits = pd.read_csv("circuits.csv")
drivers = pd.read_csv("drivers.csv")
constructor = pd.read_csv("constructors.csv")

#droping the columns we need
results = results[['raceId', 'driverId', 'constructorId', 'grid', 'position']]

circuits = circuits[['circuitId', 'name']]
circuits = circuits.rename(columns = {"circuitId":"raceId"})

drivers = drivers[['driverId', 'forename', 'surname']]

constructor = constructor[['constructorId', 'name']]
constructor = constructor.rename(columns = {"name":"constructorName"})

#change the position name to avoid errors with position from results


#new data merge
results_driver = pd.merge(results, drivers)

results_driver_circuit = pd.merge(results_driver, circuits)

load_data = pd.merge(results_driver_circuit, constructor)

load_data.to_csv("merge_data.csv", index=False)







