from collections import defaultdict 
import parser_1
def printArr(dist,parent,V):
	from_to_cost = [] 
	total_cost = 0 
	print("from \tto \tCost")
	for i in range(V-1): 
		temp = [None]*3
		temp[0]=parent[i][0]
		temp[1]=parent[i][1]
		temp[2]=round(dist[i],4)
		from_to_cost.append(temp)
		total_cost += dist[i]
		print("%d \t%d \t %.2f" % (parent[i][0],parent[i][1] ,dist[i])) 
	print('\ntotal_cost %.2f'  % (total_cost))
	print(from_to_cost)
	return from_to_cost , total_cost,'SP : BELLMAN FORD',
		 
def BellmanFord(src,graph,V): 
	parent = [[0 for x in range(2)] for y in range(V)]
	dist = [float("Inf")] * V 
	dist[src] = 0
	for i in range(V - 1): 
		for u, v, w in graph: 
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					parent[v][0]= u
					parent[v][1]=v 
					dist[v] = dist[u] + w	
	
	for u, v, w in graph: 
			if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
					print ("Graph contains negative weight cycle")
					return
	parent.pop(src)
	dist.pop(src)
					
	return printArr(dist,parent,V) 
def BELLMANFORD(from_to_cost,no_of_nodes,source):
	return BellmanFord(source,from_to_cost,no_of_nodes) 