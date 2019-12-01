import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
import pprint
from matplotlib.widgets import Slider, Button, RadioButtons
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

def LOCALCLUSTERAVERAGE(input_data):
    plt.style.use('dark_background')
    node_x_y = input_data[0]
    from_to_cost = input_data[1]
    no_of_nodes = input_data[2]
    source = input_data[3]
    total_cost = input_data[4]
    algoName = 'Local Clustering Co-effecient'
    G = nx.DiGraph(directed=True)
    for i in range(no_of_nodes):
        G.add_node(int(node_x_y[i][0]),pos=(float(node_x_y[i][1]),float(node_x_y[i][2])))
    for i in range(len(from_to_cost)):
        G.add_edge(from_to_cost[i][0],from_to_cost[i][1],weight=from_to_cost[i][2])
    edge_labels=dict([((u,v,),d['weight'])
                    for u,v,d in G.edges(data=True)])
    node_labels=[int(node[0]) for node in node_x_y]
    # pprint.pprint(nx.average_clustering(G))

    return nx.average_clustering(G)

def LocalCluster(input_data, ui):
    plt.style.use('dark_background')
    node_x_y = input_data[0]
    from_to_cost = input_data[1]
    no_of_nodes = input_data[2]
    source = input_data[3]
    total_cost = input_data[4]
    algoName = 'Local Clustering Co-effecient'
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
        edge_label_size = 5
    
    options = {
        'node_color': node_color,
        'edge_color':'orange',
        'node_size':node_size,
        'width':1,
    }
    pprint.pprint(edge_labels)
    pprint.pprint(nx.clustering(G))
    # pprint.pprint(nx.triangles(G))
    pprint.pprint(nx.transitivity(G))
    pprint.pprint(nx.average_clustering(G))
    pprint.pprint(nx.square_clustering(G))
    # pprint.pprint(nx.generalized_degree(G))
    c_n = nx.clustering(G,G.nodes)
    cnodes = G.nodes()

    color_cluster = [c_n[n] for n in cnodes]
    node_w_cc = [(k,v) for k,v in nx.clustering(G).items()]# node with clustering co-effecient
    print(node_w_cc)
    pprint.pprint(color_cluster)
    pos = nx.get_node_attributes(G,'pos')
    # fig,(ax1, ax2) = plt.subplots( 1, 2,figsize=(20, 10))
    fig,ax1 = plt.subplots( figsize=(15, 10))
    ax1.set(xlabel='Average Local Clustering Co-effecient : %.2f' %(nx.average_clustering(G)))


    ax1.set_title(algoName)
    nx.draw_networkx_nodes(G,pos,with_labels=True, nodelist=node_labels , ax=ax1, node_color = color_cluster,cmap=plt.cm.Reds)
    nx.draw_networkx_labels(G,pos,ax = ax1,node_labels=node_labels)
    nx.draw_networkx_edges(G,pos, ax = ax1,**options)
    nx.draw_networkx_edge_labels(G,pos, ax = ax1,edge_labels=edge_labels, font_size = edge_label_size)
    
    ax1.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    table_colors = [(x ,x) for x  in color_cluster]
    # fig,ax2 = plt.subplots( figsize=(7, 15))
    
    # t = plt.table(cellText = node_w_cc , colLabels = ['Edge', 'Clustering Co-effecient'], loc = 'center', cellColours =plt.cm.Reds(table_colors))
    
    
    

    qtable = QtWidgets.QTableWidget(len(color_cluster), 2)
    qtable.setMinimumHeight(800)
    qtable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    qtable.setHorizontalHeaderItem(0, QTableWidgetItem('Vertex :'))
    qtable.setHorizontalHeaderItem(1, QTableWidgetItem('Local Clustering Co-effecient :'))
    for x in range(0, len(color_cluster)):
        qtable.setItem(x,0, QTableWidgetItem( str(x)))
        qtable.setItem(x, 1, QTableWidgetItem(str(c_n[x])))
        qtable.item(x,0).setBackground(QtGui.QColor(plt.cm.Reds(table_colors)[x][0][0]* 255,plt.cm.Reds(table_colors)[x][0][1] * 255,plt.cm.Reds(table_colors)[x][0][2]* 255))
        qtable.item(x,1).setBackground(QtGui.QColor(plt.cm.Reds(table_colors)[x][0][0]* 255,plt.cm.Reds(table_colors)[x][0][1] * 255,plt.cm.Reds(table_colors)[x][0][2]* 255))
    qtable.show()

    # row_height = 0.03 
    # if len(color_cluster) > 40:
    #     row_height = 0.02
    # for cell in t.get_celld():
    #     print(cell)
    #     t[cell].set_text_props(color='black')
    #     t[cell].set_height(row_height)
    # ax2.axis('off')


    plt.show() 