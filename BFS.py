# An exmple of Breath first search
# Written and edited by Isha Suri

class node (object):
    def __init__ (self, name):
        self.name=name
        self.neigbourlist=[]
        self.visited=False

class Breathfirstsearch(object):
    def bfs(self, startnode):
        queue=[]
        queue.append(startnode)
        startnode.visited=True


        while queue:
            actualnode=queue.pop(0)
            print (actualnode.name)

            for n in actualnode.neigbourlist:
                if not n.visited:
                    n.visited=True
                    queue.append(n)


node1=node('A')
node2=node('B')
node3=node('D')
node4=node('E')
node5=node('C')

node1.neigbourlist.append(node2)
node1.neigbourlist.append(node3)
node2.neigbourlist.append(node4)
node3.neigbourlist.append(node5)

first=Breathfirstsearch()
first.bfs(node1)
