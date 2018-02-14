#An example of graph seach algorithm
# Written and edited by Isha Suri

def bfs_component(graph,start):
    #Kepp track of all visited nodes
    explored=[]
    #keep track of nodes to be checked
    queue=[start]

    #Keep looping until there are nodes to be checked
    while queue:
        #Pop First node from queue
        node=queue.pop(0)
        if node not in explored:
            #Add node to list of explored
            explored.append(node)
            neigbours=graph(node)

            #Add neigboursof node to queue
            for neigbour in neigbours:
                queue.append(neigbour)
    return explored


graph={'A':['B','C','D'],
       'B': ['A','D','E'],
       'C': ['A','F','G']
}
bfs_component(graph,'A')
