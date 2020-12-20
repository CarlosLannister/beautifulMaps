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

# Get data for places

#Gwater = ox.graph_from_place(places,  retain_all=True, simplify = False, custom_filter='["waterway"~"river"]')

#["waterway"~"stream"]
#G1 = ox.graph_from_place(place, custom_filter='["natural"~"water"]')
G1 = ox.graph_from_place(places, retain_all=True, simplify = False, custom_filter='["natural"~"water"]')
G2 = ox.graph_from_place(places, retain_all=True, simplify = False,custom_filter='["waterway"~"river"]')
Gwater = nx.compose(G1, G2)


#Gwater = ox.graph_from_place(places,  retain_all=True, simplify = False, custom_filter='["waterway"="river"]')

u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in Gwater.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)    


# List to store colors
roadColors = []
roadWidths = []

for item in data:
    if "name" in item.keys():
        if "Río" in item['name']: 
            color = "#5dc1b9"
            linewidth = 1.8
        else:
            color = "#5dc1b9"
            linewidth = 0.5
    else:
        color = "#5dc1b9"
        linewidth = 0.5
    roadColors.append(color)    
    roadWidths.append(linewidth)


fig, ax = ox.plot_graph(Gwater, node_size=0,figsize=(27, 40), bbox = (north, south, east, west),
                        dpi = 300, save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("alcalaWater.png", dpi=300, bbox_inches='tight', format="png", facecolor=fig.get_facecolor(), transparent=True)