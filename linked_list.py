# An example of creating linklist
# Written and modified by Isha Suri
class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode= None

class linklist(object):
    def __init__(self):
        self.head=None
        self.size=0

    def insertstart(self,data):
        self.size=self.size+1
        newnode=Node(data)

        if not self.head:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode

    def size(self):
        return self.size

    def size2(self):
        actualnode=self.head
        size=0

        while actualnode is not None:
            size=size+1
            actualnode=actualnode.nextnode
        return size

    def insertend(self,data):
        self.size=self.size+1
        newnode=Node(data)
        actualnode=self.head

        while actualnode.nextnode is not None:
            actualnode=actualnode.nextnode

        actualnode.nextnode=newnode

    def traverselist(self):
        actualnode=self.head

        while actualnode is not None:
            print (actualnode.data)
            actualnode=actualnode.nextnode


    def remove(self,data):
        if self.head is None:
            return
        self.size=self.size-1
        actualnode=self.head
        previosnode=None

        while actualnode.data!=data:
            previosnode=actualnode
            actualnode=actualnode.nextnode

        if previosnode is None:
            self.head=actualnode.nextnode
        else:
            previosnode.nextnode=actualnode.nextnode

list=linklist()
list.insertstart(12)
list.insertstart(100)
list.insertstart(1000)
list.insertend(0)
list.traverselist()
