from collections import deque

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    ################################ Depth First Search ################################

    # Pre Order Code (root-left-right)
    def preorder(self, node):
        if node == None:
            return
        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

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

    ################################ Breadth First Search ################################

    # Level Order
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
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1 + max(left_h, right_h)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


T1 = Tree("Drinks")
T2 = Tree("Hot")
T3 = Tree("Cold")
T4 = Tree("Coffee")
T5 = Tree("Tea")
T6 = Tree("Cola")
T7 = Tree("Fanta")

T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5
T3.left = T6
T3.right = T7

T1.preorder(T1)
print()
T1.inorder(T1)
print()
T1.postorder(T1)
print()
print(T1.level_order(T1))
print(f"Height of Root: {T1.height(T1)}")