def PARSER(filename):
    print(filename)
    f = open("benchmark\\"+str(filename)+".txt", "r")

    # READ_FILE
    content  = f.read().splitlines()

    #REMOVE EMPTY ARRAY
    content = [i for i in content if i] 
    #IN 2-D ARRAY
    for i in range (len(content)):
        content[i]=content[i].split()
    content.pop(0)

    #NODE_COUNT
    no_of_nodes = int(content[0][0])

    #NODE _ X _ Y in one ARRAY 
    node_x_y = [None]*(no_of_nodes)
    for i in range (1,no_of_nodes+1):
        node_x_y[i-1] = content[i]
    from_to_cost = []
    for i in range (no_of_nodes+1,len(content)-1):
        j=1
        while j < len(content[i]):
            temp = [None]*3
            temp[0] = i - no_of_nodes - 1
            temp[1] = int(content[i][j])
            j=j+2
            temp[2] = int(float(content[i][j]))/10000000
            j=j+2
            from_to_cost.append(temp)
    source = int(content[len(content)-1][0])
    f.close()
    # print(no_of_nodes)
    # print(node_x_y)
    # print(from_to_cost)
    # print(source)
    # print(matrix)
    return node_x_y , from_to_cost , no_of_nodes , source
# PARSER()