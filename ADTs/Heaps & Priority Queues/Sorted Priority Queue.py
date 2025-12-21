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


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        """Insert item in sorted order (smallest key first)."""
        item = self.Item(key, value)

        # Find correct position
        i = len(self.data) - 1
        while i >= 0 and item < self.data[i]:
            i -= 1

        self.data.insert(i + 1, item)

    def min(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")

        item = self.data[0]
        return (item.key, item.value)

    def remove_min(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")

        item = self.data.pop(0)
        return (item.key, item.value)
