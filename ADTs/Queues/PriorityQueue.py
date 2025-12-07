class PriorityQueueBase:
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key  # compare by key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def add(self, key, value):
        item = self.Item(key, value)
        self.data.append(item)

    def find_min(self):
        if self.is_empty():
            print("Priority Queue is Empty")
            return None
        small = 0
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[small]:
                small = i
        return small

    def min(self):
        p = self.find_min()
        if p is None:
            return None
        item = self.data[p]
        return (item.key, item.value)

    def remove_min(self):
        p = self.find_min()
        if p is None:
            return None
        item = self.data.pop(p)
        return (item.key, item.value)


# Example usage
UPQ = UnsortedPriorityQueue()
UPQ.add(6083, "Kumail")
UPQ.add(6073, "Ahmed")
UPQ.add(6001, "Sufyan")
UPQ.add(6123, "Adil")

print("Minimum:", UPQ.min())
