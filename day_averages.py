import pandas as pd
import sys

def dayAverages(file):
    data = pd.read_csv(file)
    
    data["Date & Time"] = pd.to_datetime(data["Date & Time"])
    data = data.set_index(data["Date & Time"])
    
    year = str(data["Date & Time"][1].year)
    
    data = data.resample('D').mean()
    data.to_csv('./resources/daily_averages' + year +'.csv')
    

args = sys.argv
if (len(args) == 2):
    dayAverages(args[1])
else:
    for i in range(2014,2018):
        file = './resources/raw_data' + str(i)+ '.csv'
        dayAverages(file)
