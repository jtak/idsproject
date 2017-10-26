import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data15 = pd.read_csv('./resources/month_average_weeks2015.csv')

def plot_aq(data, month, placename, year):
    march = data[data['Date & Time'] == month]
    
    daynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    monthnames = ['asd', 'January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    colours = ['r', 'g', 'b', 'y', 'orange']
        
    fig, ax1 = plt.subplots(figsize=(8, 6), dpi=100)
        
    for weekday in range(5):
        placedata = march[placename].iloc[24*weekday:24*(weekday+1)]
        asd, = ax1.plot(list(range(0,24)), placedata, linewidth=2.5, color=colours[weekday], label = daynames[weekday])
        plt.legend(bbox_to_anchor = (1.15,1), loc = 2, borderaxespad = 0)
    
    plt.title(placename + ', ' + monthnames[month] + str(year))
    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Air quality ")
        
    ax1.set_ylim(0, 125)
    
    plt.subplots_adjust(right=0.70)
    
    plt.savefig(placename + monthnames[month] + str(year) +'.png')

months = [3,6,9,10]
places = ['Mäkelänkatu2', 'Mannerheimintie', 'Tikkurila3']

for val in places:
    for i in months:    
        plot_aq(data15, i, val,2015)