import pandas as pd
import numpy as np
import sys

args = sys.argv

file = args[1]

data = pd.read_csv('./resources/' + file)

data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
data = data.set_index(data["Date & Time"])
year = data["Date & Time"][1].year
data = data.resample('D').mean()
data.to_csv('./resources/paivakeskiarvot' + year +'.csv')
