class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def count_Nodes(self):
        return self.size

    # Insert at Beginning Code
    def insert_at_Beginning(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head  # Fixed: new node points forward to old head
            self.head.prev = new_node  # old head points back to new node
            self.head = new_node       # new node becomes the head
            self.size += 1

    # Insert at End Code
    def insert_at_End(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.size += 1

    # Insert at Position Code
    def insert_at_Position(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_Beginning(val)  # Fixed: was insert_at_Head
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position Out of Bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:  # Only one node
            self.head = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:  # Only one node
            self.head = None
            self.size -= 1
        else:
            current = self.head
            while current.next:  # Go to the last node
                current = current.next
            current.prev.next = None  # Remove the last node
            self.size -= 1

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        if current is None:
            print("Position Out of Bounds")
            return
        # Update the previous node's next pointer
        if current.prev:
            current.prev.next = current.next
        # Update the next node's prev pointer
        if current.next:
            current.next.prev = current.prev
        self.size -= 1


    def traverse_forward(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next  # Move forward
        print()

    def traverse_reverse(self):
        current = self.head
        while current.next:  # Go to the last node
            current = current.next
        while current:
            print(current.val, end=" ")
            current = current.prev  # Move backward
        print()

    def reverse_Doubly_Linked_List(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            return
        current = self.head
        previous = None
        while current is not None:
            front = current.next
            current.next = previous
            current.prev = front
            previous = current
            current = front
        self.head = previous

DLL = DoublyLinkedList()
DLL.insert_at_Beginning('a')
DLL.insert_at_End('b')
DLL.insert_at_End('c')
DLL.insert_at_End('x')
DLL.insert_at_End('y')
DLL.insert_at_End('z')
DLL.traverse_forward()
DLL.reverse_Doubly_Linked_List()
DLL.traverse_forward()