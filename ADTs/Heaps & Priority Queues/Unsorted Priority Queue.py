class PriorityQueueBase:
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        self.data.append(self.Item(key, value))

    def _find_min_item(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")

        small = 0
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[small]:
                small = i
        return small

    def min(self):
        idx = self._find_min_item()
        item = self.data[idx]
        return (item.key, item.value)

    def remove_min(self):
        idx = self._find_min_item()
        item = self.data.pop(idx)
        return (item.key, item.value)

UPQ = UnsortedPriorityQueue()
UPQ.add(6083, "Kumail")
UPQ.add(6073, "Ahmed")
UPQ.add(6001, "Sufyan")
UPQ.add(6123, "Adil")

print("Minimum:", UPQ.min())
print("Removed:", UPQ.remove_min())
print("New Minimum:", UPQ.min())
