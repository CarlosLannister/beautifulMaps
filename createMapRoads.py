# To make maps
import networkx as nx
import osmnx as ox
import requests
import matplotlib 
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D

from PIL import Image, ImageOps, ImageColor, ImageFont, ImageDraw 


# Define city/cities
places = ["Madrid, Spain"]
# Center of map
latitude = 40.4381311
longitude = -3.8196194

# Bbox sides
north = latitude + 0.15
south = latitude - 0.15
east = longitude + 0.5
west = longitude - 0.4

bgcolor = "#061529"

# Get data for places

G = ox.graph_from_place(places,  retain_all=True, simplify = True, network_type='all')

u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)    
# List to store colors
roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#a6a6a6" 
            
        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            color = "#676767"
            
        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            color = "#454545"
            
        elif item["length"] > 400 and item["length"] <= 800:
            color = "#d5d5d5"
            linewidth = 0.35
        else:
            color = "#ededed"
            linewidth = 0.45
    else:
        color = "#a6a6a6"
        linewidth = 0.10
            
    roadColors.append(color)
    roadWidths.append(linewidth)
            
# List to store linewidths

'''
for item in data:
    if "footway" in item["highway"]:
        linewidth = 0.25
    else:
        linewidth = 0.5
        
    roadWidths.append(linewidth)
'''

# Make Map 
fig, ax = ox.plot_graph(G, node_size=0,figsize=(27, 40), bbox = (north, south, east, west),
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("alcalaRoads.png", dpi=300, bbox_inches='tight', format="png", facecolor=fig.get_facecolor(), transparent=False)