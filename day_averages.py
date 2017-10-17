import pandas as pd
import numpy as np
import sys

args = sys.argv

file = args[1]

data = pd.read_csv(file)

data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
data = data.set_index(data["Date & Time"])
year = str(data["Date & Time"][1].year)
data = data.resample('D').mean()
data.to_csv('./resources/daily_averages' + year +'.csv')
