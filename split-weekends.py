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
weekdays = data[data['weekdays'] < 5]

weekends = weekends.drop(['weekdays'], 1)
weekdays = weekdays.drop(['weekdays'], 1)

filename = file.split(".")

weekdays.to_csv(filename[0] + "_weekdays.csv")
weekends.to_csv(filename[0] + "_weekends.csv")