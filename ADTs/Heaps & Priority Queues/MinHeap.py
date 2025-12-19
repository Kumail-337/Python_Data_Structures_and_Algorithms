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


class MinHeap(PriorityQueueBase):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)

    def _has_right(self, j):
        return self._right(j) < len(self.data)

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.data[j], self.data[parent] = self.data[parent], self.data[j]
            self._upheap(parent)

    def _downheap(self, j):                      # ✅ ADDED
        if self._has_left(j):
            left = self._left(j)
            small = left

            if self._has_right(j):
                right = self._right(j)
                if self.data[right] < self.data[left]:
                    small = right

            if self.data[small] < self.data[j]:
                self.data[j], self.data[small] = self.data[small], self.data[j]
                self._downheap(small)

    def add(self, key, value):
        self.data.append(self.Item(key, value))
        self._upheap(len(self.data) - 1)

    def min(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        item = self.data[0]
        return (item.key, item.value)

    def remove_min(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        item = self.data.pop()
        if not self.is_empty():                  # ✅ SAFETY FIX
            self._downheap(0)
        return (item.key, item.value)

    def show_list(self):
        return [(item.key, item.value) for item in self.data]

# -------- TEST --------
H = MinHeap()

H.add(6083, "Kumail")
H.add(6073, "Ahmed")
H.add(6001, "Sufyan")
H.add(6123, "Adil")

print("Min:", H.min())
print("Removed:", H.remove_min())
print("New Min:", H.min())