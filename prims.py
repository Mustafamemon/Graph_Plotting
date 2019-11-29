import sys 
import parser_1

def printMST(parent,V,graph):
	from_to_cost = [] 
	total_cost = 0 
	print ("Edge \tWeight")
	for i in range(V):
		print(parent[i])
		if parent[i] != None:
			temp = [None]*3 
			total_cost += graph[i][parent[i]]
			print (parent[i], "-", i, "\t",  graph[i][parent[i]])
			temp[0]=parent[i]
			temp[1]=i
			temp[2]=round(graph[i][parent[i]],2)
			from_to_cost.append(temp)
	print ("total_cost : %.2f "% (total_cost))
	return  from_to_cost,total_cost,'MST : PRIMS',

def minKey(key, mstSet,min_index,V): 
	min = sys.maxsize 

	for v in range(V): 
		if key[v] < min and mstSet[v] == False: 
			min = key[v] 
			min_index = v 

	return min_index 

def primMST(graph,V,source): 
	key = [sys.maxsize] * V 	
	parent = [None] * V 
	key[source] = 0
	mstSet = [False] * V 
	parent[0] = -1  

	for cout in range(V): 
		u = minKey(key, mstSet,0,V) 
		mstSet[u] = True
		for v in range(V): 
			if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]: 
					key[v] = graph[u][v] 
					parent[v] = u 
	return printMST(parent,V,graph) 

def PRIMS(from_to_cost,no_of_nodes,source):
	graph = [[0 for x in range(no_of_nodes)] for y in range(no_of_nodes)] 
	for i in range (len(from_to_cost)):
		graph[from_to_cost[i][0]][from_to_cost[i][1]] = from_to_cost[i][2]
	return primMST(graph,no_of_nodes,source)

