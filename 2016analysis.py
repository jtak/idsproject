import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data = pd.read_csv("/Users/kasimiraula/Downloads/Ilmanlaatuindeksit2015.xls", sheetname = "Indeksit")

#da = data.resample('D').mean()


months = ["January","February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
times = ["23:59", "01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00", "10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00", "20:00","21:00","22:00","23:00"]

month = data["2016-January"]
hdata = month[month["Time"] == "01:00"]

month_houravg = pd.DataFrame(columns = data.columns.values)
i = 0
for val in months:
    month = data['2016-' + val]
    for hour in times:
        hourdata = month[month['Time'] == hour]
        hourdata = hourdata.drop(['Time'],1)
        month_houravg = month_houravg.append(np.mean(hourdata, axis = 0), ignore_index = True)
        month_houravg['Time'][i] = val + " " + hour
        i +=1


#format="%m/%d/%Y %I:%M:%S %p")
#month_houravg['Time'] = pd.to_datetime(month_houravg['Time'], format="%m %H:%M")
#month_houravg = month_houravg.set_index(month_houravg['Time'])
#month_houravg = month_houravg.drop(['Time'],1)

month_houravg.to_csv("month_houravg.csv")

'''mansku1 = month_houravg["Mannerheimintie"][:24]
mansku2 = month_houravg["Mannerheimintie"][24:48].reset_index(drop= True)
mk1 = month_houravg["Mäkelänkatu2"][:24]
mk2 = month_houravg["Mäkelänkatu2"][24:48].reset_index(drop= True)
plt.plot(mansku1)
plt.plot(mansku2)
plt.plot(mk1)
plt.plot(mk2)

for val in month_houravg.columns.values:
    print(val)
    intervals = [24*(i+1) for i in list(range(12))]
    i = 0
    for intv in intervals:
        #plt.scatter(x = list(range(24)), y = month_houravg["Leppävaara4"][i:intv].reset_index(drop= True), s = (np.array(month_houravg["Leppävaara4"])), alpha=0.4)
        #plt.plot(month_houravg[val][i:intv].reset_index(drop= True),label=month_houravg['Time'][i])
        #plt.xticks(np.arange(0, 23, 2))
        i=intv


for val in month_houravg.columns.values:
    plt.plot(month_houravg[val])
    month_houravg.add(pd.Series(np.mean(hourdata16, axis = 0), name = "January " + str(val)))
'''