class Node:
    def __init__(self, item = None, next = None):
        self.item = item 
        self.next = next

class Stack:
    def __init__(self, top = None):
        self.top = top
        self.item_count = 0

    def is_empty(self):
        return self.top == None
    def push(self, data):
        n = Node(data, self.top)
        self.top = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.top.item
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack is Empty')
        
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count
    

# n = Node()
s = Stack()
s.push(34)
s.push(32)
s.push(56)
print(s.size())