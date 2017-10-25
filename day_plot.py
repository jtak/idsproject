import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def findIndex(value):
    if value <= 50: 
        return 0
    elif value <= 75:
        return 1
    elif value <= 100:
        return 2
    elif value <= 150:
        return 3
    else: 
        return 4

def makeImages(year):
    data = pd.read_csv('./resources/daily_averages' + str(year) +'.csv')
    data["Date & Time"] = pd.to_datetime(data["Date & Time"])
    im =plt.imread('./resources/Seutukartta3.png')
    plt.imshow(im)
    
    colors = ['green','gold', 'orange', 'red', 'purple']
    coord = {'Mannerheimintie' : (775,805), 'Mäkelänkatu2':(785,725), 'Kallio2':(790,755), 'Vartiokylä':(1052,623),'Leppävaara4':(550,635), 'Tikkurila3':(935,400), 'Luukki': (330,310)}
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    xsis = []
    ysis = []
    for key in coord:
        x,y = coord[key]
        xsis.append(x)
        ysis.append(y)
        
    for i in range(0,len(data)):
        sizes = []
        colors1 = []
        for key in coord:
            size = data[key][i]
            sizes.append(size/2)
            idx = findIndex(size)
            colors1.append(colors[idx])
        scat = plt.scatter(xsis,ysis, c= colors1, s = sizes, edgecolors = 'black')
        plt.axis('off')
        day = data['Date & Time'][i].date()
        text = plt.text(580,1000, str(day) + ' ' +weekdays[day.weekday()])
        plt.savefig('./Images/'+ str(year)+'/' +str(day) + '.jpg', transparent = True, bbox_inches = 'tight', pad_inches = 0, dpi= 300)
        scat.remove()
        text.remove()

args = sys.argv
if len(args) == 2:
    makeImages(args[1])
else:
    for year in range(2014,2018):
        makeImages(year)

#make gif : imagemagick : convert -delay 50 -loop 0 *.jpg animated.gif