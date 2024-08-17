class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        return self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('Stack is empty')
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Stack is empty')
        
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError('No insertion')
    

s = Stack()
s.push(5)
s.push(34)
s.push(7)
print(s.size())

s.pop()
print(s.peek())


