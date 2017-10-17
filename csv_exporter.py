import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data = pd.read_excel("/Users/kasimiraula/Downloads/Ilmanlaatuindeksit2016.xlsx", sheetname = "Indeksit")
data['Date & Time'] = data['Date & Time'].str.replace('24:00', '23:59')
data.replace(["NoData", "OffScan"], np.NaN, inplace=True)

dn = data['Date & Time'].str.split(' ')
data['Time'] = [val[1] for val in dn]


data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
data = data.set_index(data["Date & Time"])
data = data.drop(['Date & Time'],1)

data.to_csv("raw_data2016.csv")


