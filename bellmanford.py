from collections import defaultdict 
import parser_1
def printArr(dist,from_to_cost,V):
	total_cost = 0 
	print("from \tto \tCost")
	for i in range(V-1): 
		total_cost += dist[i]
		print("%d \t%d \t %.2f" % (from_to_cost[i][0],from_to_cost[i][1] ,dist[i])) 
	print('\ntotal_cost %.2f'  % (total_cost))
	return from_to_cost , total_cost,'SP : BELLMAN FORD',
		 
def BellmanFord(src,graph,V): 
	from_to_cost = [[0 for x in range(3)] for y in range(V)]
	dist = [float("Inf")] * V 
	dist[src] = 0
	for i in range(V - 1): 
		for u, v, w in graph: 
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					from_to_cost[v][0]= u
					from_to_cost[v][1]=v 
					from_to_cost[v][2]=w
					dist[v] = dist[u] + w	
	
	for u, v, w in graph: 
			if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
					print ("Graph contains negative weight cycle")
					return
	from_to_cost.pop(src)
	dist.pop(src)
					
	return printArr(dist,from_to_cost,V) 
def BELLMANFORD(from_to_cost,no_of_nodes,source):
	return BellmanFord(source,from_to_cost,no_of_nodes) 