import sys 
import parser_1

def printSolution(dist,from_to_cost,V): 
	total_cost  = 0 
	print("from \tto \tCost")
	for node in range(V-1): 
		total_cost += dist[node]
		print('%d \t%d \t%.2f'%(from_to_cost[node][0],from_to_cost[node][1] , dist[node]))
	print('\ntotal_cost %.2f'  % (total_cost)) 
	return from_to_cost,total_cost,'SP : DIJKSTRA'

def minDistance(dist, sptSet,V): 
	min = sys.maxsize 

	for v in range(V): 
		if dist[v] < min and sptSet[v] == False: 
			min = dist[v] 
			min_index = v 

	return min_index 

def dijkstra(src,graph,V): 
	dist = [sys.maxsize] * V 
	dist[src] = 0
	sptSet = [False] * V 
	from_to_cost = [[0 for x in range(3)] for y in range(V)]
	for cout in range(V): 
		u = minDistance(dist, sptSet,V) 
		sptSet[u] = True
		for v in range(V): 
			if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]: 
					print(v)
					from_to_cost[v][0]=u
					from_to_cost[v][1]=v
					from_to_cost[v][2]= graph[u][v]
					dist[v] = dist[u] + graph[u][v]
	print(from_to_cost)			
	from_to_cost.pop(src)
	dist.pop(src)	
	return printSolution(dist,from_to_cost,V) 

def DIJKSTRA(from_to_cost,no_of_nodes,source):
	graph = [[0 for x in range(no_of_nodes)] for y in range(no_of_nodes)] 
	for i in range (len(from_to_cost)):
		graph[from_to_cost[i][0]][from_to_cost[i][1]] = from_to_cost[i][2]
	return dijkstra(source,graph,no_of_nodes); 

