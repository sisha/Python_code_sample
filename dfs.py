# An example of Depth First binary_search
# Written and edited by Isha Suri


class node(object):
    def __init__ (self, name):
        self.name=name
        self.neigbourlist=[]
        self.visited=False

class Depthfirstsearch(object):
    def dfs (self, startnode):
        startnode.visited=True
        print(startnode.name)

        for n in startnode.neigbourlist:
            if not n.visited:
                self.dfs(n)

node1=node('A')
node2=node('B')
node3=node('D')
node4=node('E')
node5=node('C')

node1.neigbourlist.append(node2)
node1.neigbourlist.append(node3)
node2.neigbourlist.append(node4)
node3.neigbourlist.append(node5)

second=Depthfirstsearch()
second.dfs(node1)
