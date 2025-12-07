class Node:
    def __init__(self,val,next = None):
        self.value = val
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
        self.n = 0

    def length(self):
        return self.n

    def is_empty(self):
        return self.length() == 0

    def push(self,e):
        node = Node(e)
        if self.is_empty():
            self.head = node
            self.n += 1
        else:
            node.next = self.head
            self.head = node
            self.n += 1

    def pop(self):
        if self.is_empty():
            print("Linked Stack is Empty")
        else:
            self.head = self.head.next
            self.n -= 1

    def traversal(self):
        if self.is_empty():
            print("Linked Stack is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.value,"->",end=" ")
                current = current.next
            print()

    def product(self):
        if self.is_empty():
            print("Linked Stack is Empty")
            return None
        else:
            node_Product = 1
            current = self.head
            while current is not None:
                node_Product *= current.value
                current = current.next
            return node_Product

    # def sum(self):
    #     if self.is_empty():
    #         print("Linked Stack is Empty")
    #         return None
    #     else:
    #         current = self.head
    #         node_sum = 0
    #         while current is not None:
    #             node_sum += current.value
    #             current = current.next
    #         return node_sum

    def sum_helper(self,node):
        if node is None:
            return 0
        else:
            return node.value + self.sum_helper(node.next)

    def sum(self):
        if self.is_empty():
            print("Linked Stack is Empty")
            return None
        else:
            return self.sum_helper(self.head)

LS1 = LinkedStack()
LS1.push(7)
LS1.push(6)
LS1.push(8)
LS1.push(4)
LS1.push(1)
LS1.traversal()
print("Sum of Nodes =", LS1.sum())