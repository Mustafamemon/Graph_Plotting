import parser_1

undefined = float('inf')
def floydWarshall(graph,path,V,src,node): 
    dist = graph
    for k in range(V): 
        for i in range(V): 
            for j in range(V):
                if(dist[i][j] > dist[i][k]+ dist[k][j]):
                    dist[i][j] = dist[i][k]+ dist[k][j]
                    path[i][j] = path[k][j]
    total_cost = 0
    node[src]=-1
    from_to_cost = [] 
    k  = (len(path[src]))-1
    dest = node[k]
    node[k]=-1
    for i in range((len(path[src]))-1,0,-1):
        temp = [None]*3
        temp[1]= dest 
        temp[0]=path[src][k]
        temp[2]=round(dist[src][k],4)
        total_cost += dist[src][k]
        from_to_cost.append(temp)
        if (path[src][k]== src or node[path[src][k]]==-1):
            for j in range((len(path[src]))-1,-1,-1):
                if(node[j]!=-1):
                    k=j
                    dest = node[k]
                    node[k] = -1
                    print(k)
                    break             
        else :
            dest = path[src][k]
            node[path[src][k]] = -1
            k  = path[src][k]
        
    return printSolution(dist,path,V,from_to_cost,total_cost) 


def printSolution(dist,path,V,from_to_cost,total_cost): 
    print ("COST TABLE : \n\n" )
    for i in range(V): 
        for j in range(V): 
            print('%.2f'% (dist[i][j]),end='\t')
        print('')
    print ("\nPATH TABLE : \n\n" )
    for i in range(V): 
        for j in range(V): 
            print('%d'% (path[i][j]),end='\t')
        print('')
    print ("\nSOURCE \t DEST \t COST : \n" )
    for i in range(len(from_to_cost)-1): 
        print("%d \t %d \t %.2f" %(from_to_cost[i][0],from_to_cost[i][1],from_to_cost[i][2]))
    print('\ntotal_cost %.2f'  % (total_cost))
    return from_to_cost , total_cost ,'FLOYD WARSHALL'


def FLOYDWARSHALL(from_to_cost,no_of_nodes,source,node_x_y):
    node = [int(i[0]) for i in node_x_y]
    graph = [[undefined for x in range(no_of_nodes)] for y in range(no_of_nodes)] 
    for i in range (len(from_to_cost)):
        graph[from_to_cost[i][0]][from_to_cost[i][1]] = from_to_cost[i][2]

    path = [[-1 for x in range(no_of_nodes)] for y in range(no_of_nodes)]
    for i in range (no_of_nodes):
        for j in range (no_of_nodes):
            if(i == j and graph[i][j] == undefined):
                graph[i][j] = 0 
            if(graph[i][j] != undefined and i != j):
                path[i][j] = i

    return floydWarshall(graph,path,no_of_nodes,source,node); 
