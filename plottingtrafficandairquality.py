import pandas as pd
import matplotlib.pyplot as plt

data14 = pd.read_csv('./resources/month_average_weeks2014.csv')
data15 = pd.read_csv('./resources/month_average_weeks2015.csv')
data16 = pd.read_csv('./resources/month_average_weeks2016.csv')

traffic = pd.read_csv('./resources/traffic_columns.csv')


def plot_traffic_and_aq(data, month, placename, year):    
    placetraffic = traffic[placename]
    place = data[data['Date & Time'] == month][placename]
    
    monthnames = ['asd', 'January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    daynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    colours = ['r', 'g', 'b', 'y', 'orange']
    
    
    fig, ax1 = plt.subplots(figsize=(8, 6), dpi=100)
    
    for weekday in range(0, 5):
        placedata = place.iloc[24*weekday:24*(weekday+1)]
        asd, = ax1.plot(list(range(0,24)), placedata, linewidth=2.5, color=colours[weekday], label = daynames[weekday])
        plt.legend(bbox_to_anchor = (1.15,1), loc = 2, borderaxespad = 0)

    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Air quality ")
    
    ax2 = ax1.twinx()
    ax2.bar(left= list(range(24)), height=placetraffic[24:], label="Cars", alpha = 0.5)
    
    ax2.set_ylabel("Cars")
    ax1.set_ylim(0, 125)
    kuva = "./" + placename + str(month) + str(year)
    plt.title(placename + ", " + monthnames[month] + " " + str(year))
    plt.legend()
    
    plt.subplots_adjust(right=0.70)
    plt.savefig(kuva)

plot_traffic_and_aq(data15, 3, 'Kallio2', 2015)

interesting_places = ['Mannerheimintie', 'Mäkelänkatu2', 'Kallio2', 'Tikkurila3', 'Vartiokylä']
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for place in interesting_places:
    for month in months:
        plot_traffic_and_aq(data16, month, place, 2016)
