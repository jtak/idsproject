import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data17 = pd.read_csv("Ilmanlaatuindeksit2017.csv")

data17['Date & Time'] = data17['Date & Time'].str.replace('24:00', '00:00')


dn = data17['Date & Time'].str.split(' ')
data17['Time'] = [val[1] for val in dn]

data17["Date & Time"] = pd.to_datetime(data17["Date & Time"], dayfirst=True)
data17 = data17.set_index(data17["Date & Time"])

print(data17['Date & Time'].head(30))

data17 = data17.drop(['Date & Time'],1)

# jan = data17.loc["01-2017"]
#
# print(jan)
# jan = jan.groupby(jan['Time'][:24]).mean()
# print(jan)

