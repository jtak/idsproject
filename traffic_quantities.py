import pandas as pd

data_all = pd.read_excel("/Users/kasimiraula/Documents/projektit/IDS - Airquality/idsproject/resources/excel-files/hki_liikennemaarat.xls")
traf_val = ['MANNERHEIMINTIE', 'MAKELANKATU', 'HELSINGINKATU', 'ITAVAYLA', 'TIKKURITIE','TURUNVAYLA']
ch = data_all[data_all['nimi'] == 'MANNERHEIMINTIE']
data_all = data_all[data_all['vuosi'] > 2013]
data_all = data_all.reset_index()
data_all = data_all.iloc[:,[2,5,6,7,-1]]

a = data_all[data_all['nimi'] == 'MANNERHEIMINTIE']
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

def discard_direction():
    new = []
    for indx in list(range(0,len(data), 48)):
        for val in list(range(indx, indx+24)):
            unit = data.iloc[val]
            cars = unit['autot'] + data.iloc[val+24]['autot']
            new.append([unit['nimi'],unit['aika'],unit['vuosi'],cars])
    return pd.DataFrame(new, columns = ['nimi','aika','vuosi','autot'])


data = data.reset_index(drop = True)
data = discard_direction()



