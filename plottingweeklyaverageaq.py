import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data15 = pd.read_csv('./resources/month_average_weeks2015.csv')

march = data15[data15['Date & Time'] == 3]

daynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
colours = ['r', 'g', 'b', 'y', 'orange']
    
fig, ax1 = plt.subplots(figsize=(8, 6), dpi=100)
    
for weekday in range(5):
    placedata = march['Kallio2'].iloc[24*weekday:24*(weekday+1)]
    asd, = ax1.plot(list(range(0,24)), placedata, linewidth=2.5, color=colours[weekday], label = daynames[weekday])
    plt.legend(bbox_to_anchor = (1.15,1), loc = 2, borderaxespad = 0)

plt.title('Kallio2, March 2015')
ax1.set_xlabel("Hour")
ax1.set_ylabel("Air quality ")
    
ax1.set_ylim(0, 125)

plt.subplots_adjust(right=0.70)

plt.savefig('KallioMarch2015.png')

