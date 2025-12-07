class DoublyLinkedBase:
    class Node:
        def __init__(self,e,p,s):
            self.e = e
            self.p = p
            self.s = s

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.s = self.tail
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def insert_between(self,e,p_n,s_n):
        node = self.Node(e,p_n,s_n)
        p_n.s = node
        s_n.p = node
        self.n += 1

    def delete_node(self,node):
        node.s.p = node.p
        node.p.s = node.s
        node = None
        self.n -= 1

class Stack(DoublyLinkedBase):
    def push(self,e):
        self.insert_between(e,self.head,self.head.s)

    def pop(self):
        self.delete_node(self.head.s)