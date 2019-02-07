class node():
    def __init__(self,x):
        self.x = x
        self.y = self.x + 10

node_lst = [node(1),node(2),node(3),node(4), node(5)]
print ([(e.x,e.y) for e in node_lst])

>>> [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15)]