import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

args = sys.argv
file = args[1]

data = pd.read_excel(file, sheetname = "Indeksit")
data['Date & Time'] = data['Date & Time'].str.replace('24:00', '23:59')
data.replace(["NoData", "OffScan"], np.NaN, inplace=True)

dn = data['Date & Time'].str.split(' ')
data['Time'] = [val[1] for val in dn]


data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
data = data.set_index(data["Date & Time"])
year = str(data["Date & Time"][0])[0:4]
data = data.drop(['Date & Time'],1)

data.to_csv("raw_data" + year +".csv")


