import pandas as pd
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.patches as mpatches
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np

data14 = pd.read_csv('./resources/month_average_weeks2014.csv')
data15 = pd.read_csv('./resources/month_average_weeks2015.csv')
traffic = pd.read_csv('./resources/traffic_columns.csv')

def plot_traffic_and_aq(month, placename):    
    placetraffic = traffic[placename]
    place = data15[data15['Date & Time'] == month][placename]
    
    monthnames = ['asd', 'January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    daynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    colours = ['r', 'g', 'b', 'y', 'orange']
    
    fig, ax1 = plt.subplots()
 
    for weekday in range(0, 5):
        placedata = place.iloc[24*weekday:24*(weekday+1)]
        asd, = ax1.plot(list(range(0,24)), placedata, color=colours[weekday], label = daynames[weekday])
        plt.legend(bbox_to_anchor = (1.15,1), loc = 2, borderaxespad = 0)

    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Air quality ")
    
    ax2 = ax1.twinx()
    ax2.bar(left= list(range(24)), height=placetraffic[:24], label="Cars", alpha = 0.5)
    
    ax2.set_ylabel("Cars")
    ax1.set_ylim(0, np.round(np.max(place.values), decimals = 0) +10)
    kuva = placename + str(month)
    plt.text(4, 2600, placename + ", " + monthnames[month])
    plt.legend()
    plt.savefig(kuva)
    
    #plt.savefig("saatana" + place + str(month) + ".png")

plot_traffic_and_aq(3, 'Mannerheimintie')
plot_traffic_and_aq(8, 'Mannerheimintie')
