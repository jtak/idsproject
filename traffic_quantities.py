import pandas as pd
import matplotlib.pyplot as plt

data_all = pd.read_excel("./resources/excel-files/hki_liikennemaarat.xls")
traf_val = ['MANNERHEIMINTIE', 'MAKELANKATU', 'HELSINGINKATU', 'ITAVAYLA', 'TIKKURITIE','TURUNVAYLA']

data_all = data_all[data_all['vuosi'] > 2013]
data_all = data_all.reset_index()
data_all = data_all.iloc[:,[2,5,6,7,-1]]

data = pd.DataFrame(columns = data_all.columns.values)
data = data.reset_index(drop = True)

for val in range(len(data_all)):
    if data_all.iloc[val]['nimi'] in traf_val:
      data = data.append(data_all.iloc[val])


def unite_rush_hours():
    new = []
    cars = 0

    for val in data.index:
        unit = data.iloc[val]
        if data.iloc[val]['aika'] % 100 != 0:
            cars += unit['autot']
        else:
            if cars > 0:
                prev = new[-1]
                prev[-1] += cars
                new.remove(new[-1])
                new.append(prev)
                cars = 0
            cars += unit['autot']
            new.append([unit['nimi'],unit['suunta'],unit['aika'],unit['vuosi'],unit['autot']])
            cars = 0
    return pd.DataFrame(new, columns = data.columns.values)

data = data.reset_index(drop = True)
data = unite_rush_hours()

def discard_traffic_direction():
    new = []
    for indx in list(range(0,len(data), 48)):
        for val in list(range(indx, indx+24)):
            unit = data.iloc[val]
            cars = unit['autot'] + data.iloc[val+24]['autot']
            new.append([unit['nimi'],unit['aika'],unit['vuosi'],cars])
    return pd.DataFrame(new, columns = ['nimi','aika','vuosi','autot'])


data = data.reset_index(drop = True)
data = discard_traffic_direction()


def combine_mansku(data):
    mansku = data[data['nimi'] == 'MANNERHEIMINTIE']
    mansku = mansku.reset_index(drop=True)
    
    new = []

    for year in range(2014, 2017):
        mansku_y = mansku[mansku['vuosi'] == year].reset_index(drop=True)
        for i in range(0, 24):
            newrow = {}
            row1 = mansku_y.iloc[i]
            row2 = mansku_y.iloc[i+24]
            newrow['nimi'] = row1.nimi
            newrow['aika'] = row1.aika
            newrow['vuosi'] = row1.vuosi
            newrow['autot'] = (row1.autot + row2.autot) // 2 # integer division
            new.append(newrow)
            
    return pd.DataFrame(new, columns = ['nimi','aika','vuosi','autot'])
            
    
mansku_avg = combine_mansku(data)
data = data[data['nimi'] != 'MANNERHEIMINTIE']
data = data.append(mansku_avg)

data = data.pivot_table('autot', ['vuosi', 'aika'], 'nimi')
data.reset_index( drop=False, inplace=True )

data.to_csv("./resources/traffic_columns.csv")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    