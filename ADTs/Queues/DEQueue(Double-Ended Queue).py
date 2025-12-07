class DEQueue:
    LIMIT = 10

    def __init__(self):
        self.data = [None] * DEQueue.LIMIT
        self.front = 0
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def first(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def last(self):
        if self.is_empty(): 
            return None
        return self.data[(self.front + self.n - 1) % DEQueue.LIMIT]

    def add_first(self, e):
        if self.n == DEQueue.LIMIT:
            print("ERROR: Queue is full")
            return None
        self.front = (self.front - 1) % DEQueue.LIMIT  # Update front pointer
        self.data[self.front] = e
        self.n += 1
        return e

    def add_last(self, e):
        if self.n == DEQueue.LIMIT:
            print("ERROR: Queue is full")
            return None
        i = (self.front + self.n) % DEQueue.LIMIT  # Fixed calculation
        self.data[i] = e
        self.n += 1
        return e

    def del_first(self):
        if self.n == 0:
            print("Queue is empty")
            return None
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % DEQueue.LIMIT
        self.n -= 1
        return value

    def del_last(self):
        if self.n == 0:  # Fixed condition
            print("ERROR: Queue is empty")
            return None
        i = (self.front + self.n - 1) % DEQueue.LIMIT  # Delete from back
        value = self.data[i]
        self.data[i] = None
        self.n -= 1
        return value

    def display_Queue(self):
        print(f"Queue: {self.data}")
        print(f"Size of Queue: {self.__len__()}")
        print(f"Front Element: {self.first()}")
        print(f"Rear Element: {self.last()}")
        print()

D1 = DEQueue()
D1.add_first(10)
D1.add_first(50)
D1.add_first(100)
D1.add_last(20)
D1.add_last(300)
D1.display_Queue()
D1.del_last()
D1.display_Queue()
D1.del_first()
D1.display_Queue()