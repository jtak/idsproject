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
    
    daynames = ['lol', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    colours = ['r', 'g', 'b', 'y', 'orange']
    
    
    """
    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
   
    host.set_xlim(0, 25,1)
    """
    fig, ax1 = plt.subplots()
    
    for weekday in range(0, 5):
        placedata = place.iloc[24*weekday:24*(weekday+1)]
        asd, = ax1.plot(list(range(0,24)), placedata, color=colours[weekday])
        patch = mpatches.Patch(color=colours[weekday], label=daynames[weekday])
        plt.legend(handles=[patch])
        #p1, = host.plot(list(range(24)), placedata)
       
        
    
    #Oli host
    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Air quality ")
    
    ax2 = ax1.twinx()
    ax2.bar(left= list(range(24)), height=placetraffic[:24], label="Cars", alpha = 0.5)
    
    ax2.set_ylabel("Cars")
    
    #par1.set_ylabel("Cars")
    ax1.set_ylim(0, np.round(np.max(place.values), decimals = 0) +10)
    kuva = placename + str(month)
    plt.text(4, 2600, placename + ", " + monthnames[month])
    plt.legend()
    plt.savefig(kuva)
    
    #plt.savefig("saatana" + place + str(month) + ".png")
    #par1.bar(left= list(range(24)), height=placetraffic[:24], label="Cars", alpha = 0.5)
    
    #host.axis["left"].label.set_color(p1.get_color())
    #par1.axis["right"].label.set_color(p2.get_color())
    
#for mesta in ['Mäkelänkatu2', 'Kallio2', 'Mannerheimintie']:
#    for kuukausi in [1, 3, 6, 9]:

plot_traffic_and_aq(3, 'Mannerheimintie')
plot_traffic_and_aq(8, 'Mannerheimintie')


'''
for val in range(0,1):
    plt.bar(left= range(0,24,1), height =(placetraffic[val*24:24*(val+1)]).reset_index(drop = True), color=cols[val], alpha=0.5)
    plt.text(val*5,(3600),str(2014+val), size = 20, color = cols[val])
    


for val in range(7):
    plotdata = kallio.iloc[24*val:24*(val+1)]
    plt.bar(left = plotdata.index[24*val:24*(val+1)], height = placetraffic[:24]/10, alpha = 0.5)
    plt.plot(plotdata)
'''