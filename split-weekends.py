import pandas as pd
import sys

args = sys.argv

file = args[1]

data = pd.read_csv(file)

data["Date & Time"] = pd.to_datetime(data["Date & Time"], dayfirst=True)
data = data.set_index(data["Date & Time"])

data['weekdays'] = data['Date & Time'].apply(lambda x: x.weekday())

data = data.drop(['Date & Time'], 1)

weekends = data[data['weekdays'] >=5]
workdays = data[data['weekdays'] < 5]

weekends = weekends.drop(['weekdays'], 1)
workdays = workdays.drop(['weekdays'], 1)

filename = file.split(".")

workdays.to_csv(filename[0] + "_workdays.csv")
weekends.to_csv(filename[0] + "_weekends.csv")