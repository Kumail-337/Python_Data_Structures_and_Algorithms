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


class MaxHeap(PriorityQueueBase):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # Index helpers
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)

    def _has_right(self, j):
        return self._right(j) < len(self.data)

    # Upheap (bubble up)
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j].key > self.data[parent].key:
            self.data[j], self.data[parent] = self.data[parent], self.data[j]
            self._upheap(parent)

    # Downheap (bubble down)
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            large = left

            if self._has_right(j):
                right = self._right(j)
                if self.data[right].key > self.data[left].key:
                    large = right

            if self.data[large].key > self.data[j].key:
                self.data[j], self.data[large] = self.data[large], self.data[j]
                self._downheap(large)

    # Add new element
    def add(self, key, value):
        self.data.append(self.Item(key, value))
        self._upheap(len(self.data) - 1)

    # Get max
    def max(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        item = self.data[0]
        return (item.key, item.value)

    # Remove max
    def remove_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        item = self.data.pop()
        if not self.is_empty():
            self._downheap(0)
        return (item.key, item.value)

    # Show heap list
    def show_list(self):
        return [(item.key, item.value) for item in self.data]

H = MaxHeap()

H.add(6083, "Kumail")
H.add(6073, "Ahmed")
H.add(6001, "Sufyan")
H.add(6123, "Adil")

print("Heap list:", H.show_list())
print("Max:", H.max())
print("Removed max:", H.remove_max())
print("New Max:", H.max())
print("Heap list after removal:", H.show_list())