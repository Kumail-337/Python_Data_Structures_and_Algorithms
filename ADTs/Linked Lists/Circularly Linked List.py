class Node:
    def __init__(self):
        self.data = None
        self.link = None

class CircularLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, value):
        temp = Node()
        temp.data = value
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.rear.link = self.front

    def deQueue(self):
        if self.front == None:
            print("Queue is empty")
            return

        value = None
        if self.front == self.rear:
            value = self.front.data
            self.front = None
            self.rear = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.link
            self.rear.link = self.front
        return value

    def traverse(self):
        if self.front == None:
            print("Queue is empty")
            return

        print("Queue elements: ", end="")
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.link
            if temp == self.front:
                break
        print()

    def display(self):
        self.traverse()
        print(f"Head of Queue: {self.front.data}")
        print(f"Tail of Queue: {self.rear.data}")

CLQ = CircularLinkedQueue()
CLQ.enQueue(10)
CLQ.enQueue(20)
CLQ.enQueue(1)
CLQ.enQueue(12)
CLQ.enQueue(2)
CLQ.enQueue(45)
CLQ.display()
CLQ.deQueue()
CLQ.deQueue()
CLQ.enQueue(100)
CLQ.display()