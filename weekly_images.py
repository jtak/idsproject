import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

colors = ['green','gold', 'orange', 'red', 'purple']
coord = {'Mannerheimintie' : (775,805), 'Mäkelänkatu2':(785,725), 'Kallio2':(790,755), 'Vartiokylä':(1052,623),'Leppävaara4':(550,635), 'Tikkurila3':(935,400), 'Luukki': (330,310)}
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
xsis = []
ysis = []

def initXYs():
    for key in coord:
        x,y = coord[key]
        xsis.append(x)
        ysis.append(y)

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
    
def drawPoints(data,index):
    sizes = []
    colors1 = []
    for key in coord:
        value = data[key][index]
        sizes.append((value/4)**1.8)
        idx = findIndex(value)
        colors1.append(colors[idx])
    return plt.scatter(xsis,ysis, c= colors1, s = sizes, edgecolors = 'black')

def drawYearAndMonth(year,month):
    if month < 10:
        text = '0' + str(month) + ' - 2014'
    else:
        text = str(month) + ' - 2014'
    return plt.text(50,100,text)
    
def drawDayAndTime(day, hour):
    if hour < 9:
        text = weekdays[day] + ' 0' +str(hour) + ':00 - 0' + str(hour +1) + ':00'
    elif hour == 9:
        text = weekdays[day] + ' 0' +str(hour) + ':00 - ' + str(hour +1) + ':00'
    else:
        text = weekdays[day] + ' ' +str(hour) + ':00 - ' + str(hour +1) + ':00'
    return plt.text(500,1000,text)

def makeImages(year, month):
    data = pd.read_csv('./resources/month_average_weeks'+str(year)+'.csv')
    data = data[data['Date & Time'] == month]
    data.reset_index(drop = True, inplace = True)
    
    image =plt.imread('./resources/Seutukartta3.png')
    plt.imshow(image)
    plt.axis('off')
        
    for i in range(len(data)):
        
        scat = drawPoints(data,i)
        yearAndMonth = drawYearAndMonth(2014,month)
        day = data['Date & Time.1'][i]
        hour = data['Date & Time.2'][i]
        dayAndTime = drawDayAndTime(day, hour)
        
        plt.savefig('./Images/'+ str(year)+'/'+str(year)+'-' +str(month) +'-'+ str(i)+'.jpg', transparent = True, bbox_inches = 'tight', pad_inches = 0, dpi= 300)
        
        scat.remove()
        yearAndMonth.remove()
        dayAndTime.remove()
        

args = sys.argv
initXYs()
if len(args) == 3:
    makeImages(int(args[1]),int(args[2]))
else:
    for year in range(2017,2018):
        makeImages(year, 3)

#make gif : imagemagick : convert -delay 50 -loop 0 *.jpg animated.gif
