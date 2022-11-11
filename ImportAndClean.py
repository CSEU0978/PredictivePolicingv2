
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def cleaning():
    crimes = pd.read_csv(r"C:\Users\parvs\Downloads\Data Sets\Chicago_Crimes_2012_to_2017.csv")

    # print('working')
    # print('Dataset Shape before drop_duplicate : ', crimes.shape)
    crimes.drop_duplicates(subset=['ID', 'Case Number'], inplace=True)
    # print('Dataset Shape after drop_duplicate: ', crimes.shape)

    crimes.drop(['Unnamed: 0', 'Case Number','Updated On','Year', 'FBI Code', 'Beat','Ward','Community Area', 'Location'], inplace=True, axis=1)

    # print(crimes.head(3))

    crimes.Date = pd.to_datetime(crimes.Date, format='%m/%d/%Y %I:%M:%S %p')
    crimes.index = pd.DatetimeIndex(crimes.Date)

    # print(crimes.shape, "\n", crimes.info())

    return crimes
