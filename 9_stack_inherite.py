from SLL import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count


s1 = Stack()
s1.push(23)
s1.push(7)
s1.push(56)
s1.push(32)
s1.pop()
s1.pop()

print(s1.peek())
print(s1.size())