import pandas as pd
import numpy as np
import sys
    
def weekAverageByMonth(year):
    file = './resources/raw_data' + str(year) +'.csv'
    #file = './resources/raw_data2015.csv'
    data = pd.read_csv(file)
    data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst = True)
    month_avg = data.groupby([data['Date & Time'].dt.month,data['Date & Time'].dt.weekday,data['Date & Time'].dt.hour]).mean()
    
    month_avg.to_csv('./resources/month_average_weeks' + str(year) + '.csv')

args = sys.argv

if(len(args) == 2):
    weekAverageByMonth(args[1])
else:
    for year in range(2014,2018):
        weekAverageByMonth(year)