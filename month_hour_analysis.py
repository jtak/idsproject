import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


def count_month_hour_avgs(file):
    data = pd.read_csv(file)
    dn = data['Date & Time'].str.split(' ')
    data['Time'] = [val[1][:-3] for val in dn]
    data["Date & Time"] = pd.to_datetime(data["Date & Time"])
    data = data.set_index(data["Date & Time"], drop = True)
        
    year = str(data["Date & Time"][1].year)
    if year == "2017":
        months = [str(i+1) for i in range(8)]
    else:
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
        
    month_houravg.to_csv("./resources/month_houravg" + year + ".csv")
    
args = sys.argv

if len(args) == 2:
    count_month_hour_avgs(args[1])
else:
    for i in range(2014,2018):
        file = "./resources/raw_data" + str(i) + ".csv"
        count_month_hour_avgs(file)