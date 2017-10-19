import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import sys

#args = sys.argv
#file = args[1]
data = pd.read_csv("/Users/kasimiraula/Documents/projektit/IDS - Airquality/idsproject/resources/raw_data2015.csv")
dn = data['Date & Time'].str.split(' ')
data['Time'] = [val[1][:-3] for val in dn]
data["Date & Time"] = pd.to_datetime(data["Date & Time"])
data = data.set_index(data["Date & Time"], drop = True)
    
year = str(data["Date & Time"][1].year)
months = [str(i+1) for i in range(12)]
times =["0" + str(i +1) + ":00" for i in range(9)]
[times.append(str(i + 10) + ":00") for i in range(14)]
times.append("23:59")
    
month_houravg = pd.DataFrame(columns = data.columns.values[:-1])
    
i = 0
for val in months:
    month = data[year + '-' + val]
    for hour in times:
        hourdata = month[month['Time'] == hour]
        hourdata = hourdata.drop(['Time'],1)
        month_houravg = month_houravg.append(np.mean(hourdata, axis = 0), ignore_index = True)
        month_houravg['Date & Time'][i] = year + "-" + val + "-1 " + " " + hour
        i +=1
    
month_houravg['Date & Time'] = pd.to_datetime(month_houravg['Date & Time'])
month_houravg = month_houravg.set_index(['Date & Time'], drop = True)
    
month_houravg.to_csv("month_houravg" + year + ".csv")