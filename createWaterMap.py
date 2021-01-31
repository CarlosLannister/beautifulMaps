import networkx as nx
import osmnx as ox


# Get data for places

'''
places = ["Madrid, Spain"]
G1 = ox.graph_from_place(places, retain_all=True, simplify = False, custom_filter='["natural"~"water"]')
G2 = ox.graph_from_place(places, retain_all=True, simplify = False,custom_filter='["waterway"~"river"]')
Gwater = nx.compose(G1, G2)
'''

point = (40.4122958, -3.6986878)
G1 = ox.graph_from_point(center_point, dist=15000, dist_type='bbox', network_type='all', 
                        simplify=True, retain_all=True, truncate_by_edge=False, clean_periphery=False, custom_filter='["natural"~"water"]')
G2 = ox.graph_from_point(center_point, dist=15000, dist_type='bbox', network_type='all', 
                        simplify=True, retain_all=True, truncate_by_edge=False, clean_periphery=False, custom_filter='["waterway"~"river"]')
Gwater = nx.compose(G1, G2)


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

# #72b1b1
# #5dc1b9
for item in data:
    if "name" in item.keys():
        if item["length"] > 400: 
            color = "#72b1b1"
            linewidth = 2
        else:
            color = "#72b1b1"
            linewidth = 0.5
    else:
        color = "#72b1b1"
        linewidth = 0.5
    roadColors.append(color)    
    roadWidths.append(linewidth)



fig, ax = ox.plot_graph(Gwater, node_size=0,figsize=(27, 40), 
                        dpi = 300, save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("waterMap.png", dpi=300, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=True)