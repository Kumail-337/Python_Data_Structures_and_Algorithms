class Queue:
    def __init__(self):
        self.queueData = []

    def is_empty(self):
        return len(self.queueData) == 0

    def enqueue(self, x):
        self.queueData.append(x)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty, Dequeue not possible")
            return None
        else:
            return self.queueData.pop(0)

    def head(self):
        if self.is_empty():
            print("Can't peek, Queue is Empty")
            return None
        else:
            return self.queueData[0]

    def tail(self):
        if self.is_empty():
            print("Can't peek, Queue is empty")
            return None
        else:
            return self.queueData[self.sizeOfQueue() - 1]

    def sizeOfQueue(self):
        return len(self.queueData)

    def displayQueue(self):
        print(f"Queue: {self.queueData}")
        print(f"Head of Queue: {self.head()}")
        print(f"Tail of Queue: {self.tail()}")
        print(f"Size of Queue: {self.sizeOfQueue()}")
        print()

Q1 = Queue()
Q1.enqueue(10)
Q1.enqueue(15)
Q1.enqueue(20)
Q1.enqueue(1)
Q1.enqueue(7)
Q1.displayQueue()
Q1.dequeue()
Q1.dequeue()
Q1.dequeue()
Q1.displayQueue()