import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
def PLOTTING(value):
    plt.style.use('dark_background')
    node_x_y = value[0]
    from_to_cost = value[1]
    no_of_nodes = value[2]
    source = value[3]
    total_cost = value[4]
    algoName = value[5]
    G = nx.DiGraph(directed=True)
    for i in range(no_of_nodes):
        G.add_node(int(node_x_y[i][0]),pos=(float(node_x_y[i][1]),float(node_x_y[i][2])))
    for i in range(len(from_to_cost)):
        G.add_edge(from_to_cost[i][0],from_to_cost[i][1],weight=from_to_cost[i][2])
    edge_labels=dict([((u,v,),d['weight'])
                    for u,v,d in G.edges(data=True)])
    node_labels=[int(node[0]) for node in node_x_y]
    node_size = 500
    node_color = 'red'
    edge_label_size = 10
    if len(node_labels) > 50:
        node_size = 200
        node_color = 'Red'
        edge_label_size = 4
    
    options = {
        'node_color': node_color,
        'edge_color':'orange',
        'node_size':node_size,
        'width':2,
    }
    pos = nx.get_node_attributes(G,'pos')
    fig,ax = plt.subplots(figsize=(15, 7))

    ax.set(xlabel='Total Cost : %.2f' %(total_cost))
    ax.set_title(algoName)
    nx.draw_networkx_nodes(G,pos,with_labels=True, nodelist=node_labels , ax=ax,**options)
    nx.draw_networkx_labels(G,pos,node_labels=node_labels)
    nx.draw_networkx_edges(G,pos,**options)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, font_size = edge_label_size)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.show() 