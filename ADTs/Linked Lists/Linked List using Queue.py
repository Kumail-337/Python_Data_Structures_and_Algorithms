class Node:
    def __init__(self,val,next = None):
        self.value = val
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def length(self):
        return self.n

    def is_empty(self):
        return self.length() == 0

    def enqueue(self,e):
        node = Node(e)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            print("Linked Queue is empty")
        else:
            self.head = self.head.next
            self.n -= 1

    def Linked_Queue_head(self):
        if self.is_empty():
            print("Can't Peek!! Linked Queue is Empty")
            return None
        else:
            return self.head.value

    def Linked_Queue_tail(self):
        if self.is_empty():
            print("Can't Peek!! Linked Queue is Empty")
            return None
        else:
            return self.tail.value

    def traversal(self):
        if self.is_empty():
            print("Linked Queue is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            print()

    def display_Linked_Queue(self):
        print("Linked Queue:")
        self.traversal()
        print(f"Head of Linked Queue: {self.Linked_Queue_head()}")
        print(f"Tail of Linked Queue: {self.Linked_Queue_tail()}")
        print(f"Size of Linked Queue: {self.length()}")
        print()

LQ = LinkedQueue()
LQ.enqueue(1)
LQ.enqueue(2)
LQ.enqueue(3)
LQ.enqueue(4)
LQ.enqueue(5)
LQ.display_Linked_Queue()
LQ.dequeue()
LQ.display_Linked_Queue()