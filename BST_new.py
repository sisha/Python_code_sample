# An example of Binary Search Tree
# Written and Edited by Isha Suri


class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif:
                if data>self.data:
                    if self.right is None:
                        self.right=node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data=data

        def lookup(self, data, parent=None):
            if data<self.data:
                if self.left is None:
                    return None, None
                else:
                    return self.left.lookup(data,self)
            elif data>self.data:
                if self.right is None:
                    return None, None
                else:
                    return self.right.lookup(data,self)
            else:
                return self, parent

        def delete()




    root=node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    node, parent=root.lookup(6)
