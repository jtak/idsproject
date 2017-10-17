import pandas as pd
import numpy as np
import sys

args = sys.argv
file = './resources/daily_averages2014.csv'

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

normalized_data.drop(['Date & Time'], 1).to_csv(
        "./resources/normalized_daily_averages" + year + ".csv")