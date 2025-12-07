from collections import deque

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Pre Order Code (root-left-right)
    def preorder(self, node):  # Fixed spelling
        if node == None:
            return
        print(node.val, end=" ")  # Changed from node.data to node.val
        self.preorder(node.left)   # Fixed spelling
        self.preorder(node.right)  # Fixed spelling

    # In Order (left-root-right)
    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.val, end=" ")
        self.inorder(node.right)

    # Post Order (left-right-root)
    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=" ")

    # Breadth First Traversal (Level Order)
    def level_order(self,node):
        result = []
        queue = deque([])
        queue.append(node)
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e.val)
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
        return result

    def height(self, node):
        if node is None:
            return -1  # use -1 so a single node has height 0
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1 + max(left_h, right_h)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


T1 = Tree(1)
T2 = Tree(2)
T3 = Tree(3)
T4 = Tree(4)
T5 = Tree(5)
T6 = Tree(6)
T7 = Tree(7)
T8 = Tree(8)
T9 = Tree(9)
T10 = Tree(10)

T3.left = T2
T3.right = T9
T8.left = T1
T8.right = T6
T4.left = T8
T4.right = T10
T5.left = T3
T5.right = T4

T5.preorder(T5)
print()
T5.inorder(T5)
print()
T5.postorder(T5)
print()
print(T5.level_order(T5))
"""
        5
       / \
      3   4
     / \  / \
    2  9 8  10
        / \
       1   6    """