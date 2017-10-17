import pandas as pd
import numpy as np


def dayAverages(year):
    data = pd.read_csv('./resources/raw_data' + year +'.csv')
    
    data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
    data = data.set_index(data["Date & Time"])
    
    data = data.resample('D').mean()
    data.to_csv('./resources/paivakeskiarvot' + year +'.csv')


for year in range(2014,2018):
    dayAverages(str(year))