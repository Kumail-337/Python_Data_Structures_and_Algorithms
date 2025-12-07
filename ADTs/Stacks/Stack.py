class Stack:
    def __init__(self):
        self.stackData = []

    def is_empty(self):
        return len(self.stackData) == 0

    def length(self):
        return len(self.stackData)

    def top_of_Stack(self):
        return self.stackData[len(self.stackData) - 1]

    def push(self,x):
        self.stackData.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            x = self.stackData.pop()
            return x

    def displayStack(self):
        print(f"Stack: {self.stackData}")
        print(f"Length of Stack: {self.length()}")
        print(f"Top of Stack: {self.top_of_Stack()} \n")

s1 = Stack()
s1.push(5)
s1.push(7)
s1.push(8)
s1.push(10)
s1.push(15)
s1.displayStack()

s1.pop()
s1.pop()
s1.displayStack()