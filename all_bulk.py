import dijkstra, bellmanford, FloydWarshall, kruskal, prims, LocalCluster
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


def get_all_results(from_to_cost,no_of_nodes,source,node_x_y, result, ui):
    kruskal_output = kruskal.kruskal(from_to_cost,no_of_nodes)
    prims_output = prims.PRIMS(from_to_cost,no_of_nodes,source)
    dijkstra_output = dijkstra.DIJKSTRA(from_to_cost,no_of_nodes,source) 
    bellman_output = bellmanford.BELLMANFORD(from_to_cost,no_of_nodes,source)
    floyd_output = FloydWarshall.FLOYDWARSHALL(from_to_cost,no_of_nodes,source,node_x_y)
    
    # print(kruskal_output)
    # print(prims_output)
    # print(dijkstra_output)
    # print(bellman_output)
    # print(floyd_output)
    kruskal_cost = kruskal_output[1]
    prims_cost = prims_output[1]
    dijkstra_cost = dijkstra_output[1]
    bellman_cost = bellman_output[1]
    floyd_cost = floyd_output[1]
    local_cluster_average = LocalCluster.LOCALCLUSTERAVERAGE(result)
    # print(kruskal_cost)
    # print(prims_cost)
    # print(dijkstra_cost)
    # print(bellman_cost)
    # print(floyd_cost)
    # print(local_cluster_average)

    data =[kruskal_cost, prims_cost, dijkstra_cost, bellman_cost, floyd_cost, local_cluster_average]
    for y in range(0, len(data)):
        # print('col test : ' + str(ui.tableWidget.item(0,y).text()))
        ui.tableWidget.item(0,y).setText(str(data[y]))
    