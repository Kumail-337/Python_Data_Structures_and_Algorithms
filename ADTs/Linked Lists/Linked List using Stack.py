class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
        self.n = 0

    def getlength(self):
        return self.n

    def is_empty(self):
        return self.getlength() == 0

    def top_of_Linked_Stack(self):
        return self.head.data

    def push(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.n += 1
        else:
            new_node.next = self.head
            self.head = new_node
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
                print(current.data,end=" ")
                current = current.next
            print()

    def display_Linked_Stack(self):
        print("Linked Stack:")
        self.traversal()
        print(f"Top of Linked Stack: {self.top_of_Linked_Stack()}")
        print(f"Length of Linked Stack: {self.getlength()}")


LS = LinkedStack()
LS.push(1)
LS.push(2)
LS.push(4)
LS.push(10)
LS.push(50)
LS.display_Linked_Stack()