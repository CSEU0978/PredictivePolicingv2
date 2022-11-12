
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plt.style.use('seaborn')
#from sklearn.tree import DecisionTreeRegressor as dtr


def cleaning():
    crimes = pd.read_csv("C:\\Users\\suran\\Desktop\\School\\1 UNIVERSITY\\BENNETT\\CSET211 Ai\\AI Hackathon\\Chicago_Crimes_2012_to_2017\\Chicago_Crimes_2012_to_2017_trimmed.csv")

    crimes=crimes.dropna(axis=0)
    iucr_codes = ['1320', '810' , '820', '460', '480']
    crimes_filt = crimes[crimes.IUCR.isin(iucr_codes)] 

    #print(crimes_filt.describe(include='all'))
    # print('working')
    # print('Dataset Shape before drop_duplicate : ', crimes.shape)
    #crimes.drop_duplicates(subset=['ID', 'Case Number'], inplace=True)
    # print('Dataset Shape after drop_duplicate: ', crimes.shape)
    #crimes.drop(['Unnamed: 0', 'Case Number','Updated On','Year', 'FBI Code', 'Beat','Ward','Community Area', 'Location'], inplace=True, axis=1)
    print(crimes_filt.head(5))

    #0crimes_filt.Date = pd.to_datetime(crimes_filt.Date, format='%m/%d/%Y %I:%M:%S %p')
    #crimes_filt.index = pd.DatetimeIndex(crimes_filt.Date)
    # print(crimes.shape, "\n", crimes.info())

    return crimes_filt
