class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def length(self):
        return self.n

    def is_empty(self):
        return self.length() == 0

    def append(self,value):
        new_Node = Node(value)

        if self.is_empty():
            self.head = new_Node
            self.n += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_Node
            self.n += 1

    def traversal(self):
        if self.is_empty():
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

    def insert_at(self,value,position):
        new_Node = Node(value)
        if position == 0:
            new_Node.next = self.head
            self.head = new_Node
            self.n += 1
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_Node
            new_Node.next = current
            self.n += 1

    def delete(self, val):
        temp = self.head
        if temp is not None:  # Changed from temp.next
            if temp.data == val:  # Changed from temp.val
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.data == val:  # Changed from temp.val
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node Not Found")

sll = SinglyLinkedList()
sll.traversal()
sll.append(5)
sll.append(100)
sll.append(20)
sll.append(25)
sll.append(12)
sll.insert_at(15,2)
sll.traversal()
print(sll.length())
sll.delete(100)
sll.traversal()
print(sll.length())