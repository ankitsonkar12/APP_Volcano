import pandas
import os
import folium
import numpy
data = pandas.read_csv("volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
map = folium.Map(location=[42.32,-82.89],zoom_start=6, tile="Stamen Terrain")
#for i, j in [[42.3168540,-82.8952112],[45.3168540,-82.67952112],[43.3168540,-82.8952112]]:
def colorman(cl):
    if cl < 1000:
        return "green"
    elif 1000 <= cl < 3000:
        return "orange"
    else:
        return "red"        
fg = folium.FeatureGroup(name="my app")

for i, j, elev in zip(lat,lon, elev):
    fg.add_child(folium.Marker(location=[i,j],popup=elev,icon=folium.Icon(colorman(elev))))
    #if elev < 3000:
 #    fg.add_child(folium.CircleMarker(location=[i,j], popup=str(elev)+" m", radius=6,fill_color=colorman(elev), color='grey',fill_opecity=.7))
   # else:
   #     map.add_child(folium.Marker(location=[i,j], popup=str(elev), icon=folium.Icon(color='red')))    

fgp = folium.FeatureGroup(name="pentagon")
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding ='utf-8-sig').read())))       
map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
    
map.save("map1.html")