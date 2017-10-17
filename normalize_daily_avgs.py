import pandas as pd
import numpy as np
import sys


def normalize(file):
    data = pd.read_csv(file)
    
    data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
    data = data.set_index(data["Date & Time"])
    
    year = str(data["Date & Time"][1].year)
    
    avgs = {}
    
    for col in data.drop(["Date & Time"], 1):
        avgs[col] = np.mean(data[col]) 
        
    normalized_data = pd.DataFrame()
    normalized_data["Date & Time"] = data["Date & Time"]
    
    for col in data.drop(["Date & Time"], 1):
        normalized_data[col] = data[col].apply(lambda x: x - avgs[col]) 
    
    normalized_data = normalized_data.drop(['Date & Time'], 1)
    normalized_data.to_csv("./resources/normalized_daily_averages" + year + ".csv")
    
args = sys.argv
if(len(args) == 2):
    normalize(args[1])
else:
    for i in range(2014,2018):
        file = './resources/daily_averages' + str(i)+ '.csv'
        normalize(file)
