import pandas as pd
import sys

def split_weekends(file):
    data = pd.read_csv(file)
    
    data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
    data = data.set_index(data["Date & Time"])
    
    data['weekdays'] = data['Date & Time'].apply(lambda x: x.weekday())
    
    year = str(data["Date & Time"][1].year)
    data = data.drop(['Date & Time'], 1)
    
    weekends = data[data['weekdays'] >=5]
    workdays = data[data['weekdays'] < 5]
    
    weekends = weekends.drop(['weekdays'], 1)
    workdays = workdays.drop(['weekdays'], 1)
    
    workdays.to_csv("./resources/workdays" + year + ".csv")
    weekends.to_csv("./resources/weekends" + year + ".csv")

args = sys.argv
file = None    
if len(args) >= 2:    
    file = args[1]
    split_weekends(file)
else:
    for year in range(2014, 2017):
        file = './resources/raw_data' + str(year) + '.csv'
        split_weekends(file)