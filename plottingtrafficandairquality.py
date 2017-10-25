import pandas as pd
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np

data14 = pd.read_csv('./resources/month_average_weeks2014.csv')
data15 = pd.read_csv('./resources/month_average_weeks2015.csv')
traffic = pd.read_csv('./resources/traffic_columns.csv')
hesari = traffic['HELSINGINKATU']
kallio = data15[data15['Date & Time'] == 10]['Kallio2']

def plot_traffic_and_aq():
#def plot_traffic_and_aq(month, place):
    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    #par2 = host.twinx()
    
    #offset = 60
    #new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    #par2.axis["right"] = new_fixed_axis(loc="right", axes=par2, offset=(offset, 0))
    
    #par2.axis["right"].toggle(all=True)

    kalliodata = kallio.iloc[24*0:24*(0+1)]
    host.set_xlim(0, 25,1)
    host.set_ylim(0, np.round(np.max(kalliodata.values), decimals = 0) +10)
    
    host.set_xlabel("Hour")
    host.set_ylabel("Air quality ")
    par1.set_ylabel("Cars")
    #par2.set_ylabel("Velocity")
    
    p1, = host.plot(list(range(24)), kalliodata, label="Air quality index")
    p2, = par1.bar(left= list(range(24)), height= hesari[:24], label="Cars", alpha = 0.5)
    #p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
    
    par1.set_ylim(0, np.round(np.max(hesari.values)))
    #par2.set_ylim(1, 65)
    
    #host.legend()
    
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    #par2.axis["right"].label.set_color(p3.get_color())


plot_traffic_and_aq()

'''
for val in range(0,1):
    plt.bar(left= range(0,24,1), height =(hesari[val*24:24*(val+1)]).reset_index(drop = True), color=cols[val], alpha=0.5)
    plt.text(val*5,(3600),str(2014+val), size = 20, color = cols[val])
    


for val in range(7):
    plotdata = kallio.iloc[24*val:24*(val+1)]
    plt.bar(left = plotdata.index[24*val:24*(val+1)], height = hesari[:24]/10, alpha = 0.5)
    plt.plot(plotdata)
'''
