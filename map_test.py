from zipfile import ZipFile
import shapefile
import geopandas as gpd
from shapely.geometry import shape  
import osr
import pandas as pd
import matplotlib.pyplot as plt


zipfile = ZipFile('./resources/maps/L41_maasto.zip')

filenames = [y for y in sorted(zipfile.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)] 
#print(filenames)

stupidtypes = ["maaAlue", "PeltoAlue", "RakennusAlue",
            "RakennusPiste", "RakennusViiva"]

maptypes = ["KiitotieViiva", "RautatieViiva", 
            "TaajamaAlue", "TieViiva", "VesiAlue", "RakennusViiva","RakennusPiste"]

done = set()
def map_type_required(map_name):
    if map_name.split(".")[0] in done:
        return False
    for type in maptypes:
        if(type in map_name):
            return True
    return False

dbf = None
shp = None
shx = None
prj = None
typestr = None
gdf = None

base = None

water = None
runways = None
rail = None
city = None
road = None
rakennus = None

for filename in filenames:
    if map_type_required(filename):
        dbf = zipfile.open(filename.split(".")[0] +  '.dbf')
        shp = zipfile.open(filename.split(".")[0] +  '.shp')
        shx = zipfile.open(filename.split(".")[0] +  '.shx')
        prj = zipfile.open(filename.split(".")[0] +  '.prj')
        done.add(filename.split(".")[0])
        typestr = filename.split(".")[0].split("_")[1]
    else:
        continue


    r = shapefile.Reader(shp=shp, shx=shx, dbf=dbf)
    #print(r.numRecords)
        
    attributes, geometry = [], []
    field_names = [field[0] for field in r.fields[1:]]  
    for row in r.shapeRecords():  
        geometry.append(shape(row.shape.__geo_interface__))  
        attributes.append(dict(zip(field_names, row.record)))  
        
    #print(row.shape.__geo_interface__)
        
    proj4_string = osr.SpatialReference(prj.read().decode('utf-8')).ExportToProj4()
    #print(proj4_string)
    
    gdf = gpd.GeoDataFrame(data = attributes, geometry = geometry, crs = proj4_string)
   
    
    if typestr == "KiitotieViiva":
        runway = gdf
    if typestr == "RautatieViiva":
        railway = gdf
    if typestr == "TaajamaAlue":
        city = gdf
    if typestr == "TieViiva":
        road = gdf
    if typestr == "VesiAlue":
        water = gdf
    if typestr == "RakennusPiste":
        rakennus = gdf
    
    
    #print(gdf.head())
    print(typestr)

print(rakennus)

base = water.plot()
cityplot = city.plot(ax=base, color='yellow')
roads = road.plot(ax=base, linewidth=0.2, color='black')
#buildings = rakennus.plot(ax=base, marker='o', markersize=0.05, color='black')

plt.savefig("maptest.png", dpi=800)
