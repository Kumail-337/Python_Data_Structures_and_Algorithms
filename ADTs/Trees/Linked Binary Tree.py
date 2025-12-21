from collections import deque


class Node:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class Position:
    def __init__(self, container, node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

    def __eq__(self, other):                     # ✅ FIX
        return type(other) is type(self) and self.node is other.node


class LinkedBinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError("Not a Position")

        if p.container is not self:
            raise ValueError("Wrong tree")

        if p.node.parent is p.node:
            raise ValueError("Node is deleted")

        return p.node

    def _make_position(self, node):
        return Position(self, node) if node else None

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def children(self, p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError("Root Exists")       # ✅ FIX
        self._root = Node(e)
        self._size = 1
        return self._make_position(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left exists")
        node.left = Node(e, parent=node)
        self._size += 1
        return self._make_position(node.left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right exists")
        node.right = Node(e, parent=node)
        self._size += 1
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        return (1 if node.left else 0) + (1 if node.right else 0)

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def delete(self, p):
        node = self._validate(p)

        if self.num_children(p) == 2:
            raise ValueError("Two children")

        child = node.left if node.left else node.right

        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child

        if child:
            child.parent = node.parent

        self._size -= 1
        node.parent = node
        return node.element

    def depth(self, p):
        if p == self.root():
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(c) for c in self.children(p))

    def preorder(self, node):
        if node == None:
            return
        print(node.element, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.element, end=" ")
        self.inorder(node.right)

    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.element, end=" ")

    def level_order(self,node):
        result = []
        queue = deque([])
        queue.append(node)
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e.element)
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
        return result

# -------- TEST --------
tree = LinkedBinaryTree()

root = tree.add_root("Drinks")
print(f"Root: {root.element()}")

left = tree.add_left(root, "Hot")
tree.add_left(left, "Tea")
tree.add_right(left, "Coffee")

right = tree.add_right(root, "Cold")
tree.add_left(right, "Cola")
tree.add_right(right, "Fanta")

print("\nPreorder:")
tree.preorder(tree._root)
print("\nIn order:")
tree.inorder(tree._root)
print("\nPost order:")
tree.postorder(tree._root)
print("\nLevel order:")
print(tree.level_order(tree._root))

print("\nDepth of Tea:", tree.depth(tree.left(left)))
print("Height of tree:", tree.height(root))