import parser_1
from collections import defaultdict 

def find(parent, i): 
	if parent[i] == i: 
		return i 
	return find(parent, parent[i]) 

def union(parent, rank, x, y): 
	xroot = find(parent, x) 
	yroot = find(parent, y) 

	if rank[xroot] < rank[yroot]: 
		parent[xroot] = yroot 
	elif rank[xroot] > rank[yroot]: 
		parent[yroot] = xroot 
	else : 
		parent[yroot] = xroot 
		rank[xroot] += 1

def KruskalMST(graph,V): 
	result =[]  
	i = 0 # An index variable, used for sorted edges 
	e = 0 # An index variable, used for result[] 

	graph = sorted(graph,key=lambda item: item[2]) 
	parent = [] ; rank = [] 
	for node in range(V): 
		parent.append(node) 
		rank.append(0) 
	while e < V -1 : 
		u,v,w = graph[i] 
		i = i + 1
		print(e) 
		x = find(parent, u) 
		y = find(parent ,v) 
		if x != y: 
			e = e + 1	
			result.append([u,v,w]) 
			union(parent, rank, x, y)			 
	print ("Following are the edges in the constructed MST")
	from_to_cost = []
	total_cost = 0
	for u,v,weight in result: 
		temp = [None]*3
		temp[0]=u
		temp[1]=v
		temp[2]=weight
		from_to_cost.append(temp)
		print ("%d -- %d == %.2f" % (u,v,weight))
		total_cost += weight
	print('total_cost : '+ str(total_cost))
	return from_to_cost,total_cost,'MST : KRUSKAL',

def kruskal(from_to_cost,no_of_nodes):
	return KruskalMST(from_to_cost,no_of_nodes)
