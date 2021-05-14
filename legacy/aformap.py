# coding: utf-8
import folium
from folium import plugins
import pandas as pd
from folium.plugins import MarkerCluster
import re
import time

m = folium.Map(location=[44.650837, 10.898436], zoom_start=16, max_zoom=19,attr='Map data &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>')
#interviewee = folium.Icon(color='red', icon='volume-up', prefix='fa')
#standard = folium.Icon(color='green', icon='volume-up', prefix='fa')

########################
#   NODES
########################
#idea from comment in https://georgetsilva.github.io/posts/mapping-points-with-folium/
df = pd.read_csv('nodes_geotagged.csv', sep='\t')
#print(df)



#marker_cluster = MarkerCluster().add_to(m)
locations = df[['lat', 'lon']]
locationlist = locations.values.tolist()
#print(locationlist)
#regex = re.compile("IN[0-9]")
#regex2 = re.compile("PL[0-9]")
#
nodes = folium.FeatureGroup(name='Punti')

marker_cluster = MarkerCluster().add_to(nodes)

for point in range(0, len(locationlist)):
    #print(str(coordinates) + ' ' + str(df['id'][point]))
    coord_lat = df['lat'][point]
    #coord_lon = df['lon'][point]
    if re.search('IN[0-9]', str(df['id'][point])) is not None:
        color = 'red'
        icon = 'volume-up'
        prefix = 'fa'
        nodename = str(df['fullname'][point])
    elif re.search('PL[0-9]', str(df['id'][point])) is not None:
        color = 'green'
        icon ='bookmark'
        prefix = 'fa'
        nodename = str(df['name'][point])
    else:
        color = 'blue'
        icon = 'volume-up'
        prefix = 'fa'
        nodename = str(df['name'][point])
        
    #print(len(coordinates))
    #print(coordinates)
    if coord_lat != 'NotAvailable':
        #The current lat and lon are swapped!!! Need to fix this in the geocoder script!
        coordinates = ([float(df['lon'][point]), float(df['lat'][point])])
        #print(str(df['name'][point]))
        
        if pd.notna(df['ialink'][point]):
            popupwri = '<h1>' + nodename + '</h1></br><iframe src="https://archive.org/embed/' + str(df['ialink'][point]) + '" width="320" height="240" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>'
        else:
            popupwri = '<h3>' + str(df['name'][point]) + '</h3>'
        
        folium.Marker(coordinates, popup=folium.Popup(popupwri, max_width=600), icon=folium.Icon(color = color, icon = icon, prefix = prefix)).add_to(marker_cluster)
    else:
        #print('WRONG COORDINATES ' + coord_lat)
        pass

#######################
#   EDGES
#######################

edges = folium.FeatureGroup(name='Network')

df_edges = pd.read_csv('../data/edges.csv', sep='\t')
lines = df_edges[['from_lat', 'from_lon']]
lineslist = lines.values.tolist()

for line in range(0, len(lineslist)):
    coordinates_from = ([float(df_edges['from_lat'][line]), float(df_edges['from_lon'][line])])
    print(coordinates_from)
    coordinates_to = ([float(df_edges['to_lat'][line]), float(df_edges['to_lon'][line])])
    coordinates_edge = ([coordinates_from, coordinates_to])
    edges.add_child(folium.PolyLine(coordinates_edge, weight=2, opacity=1))

m.add_child(nodes)
m.add_child(edges)
m.add_child(folium.LayerControl())


m.save('gh-pages/index.html')