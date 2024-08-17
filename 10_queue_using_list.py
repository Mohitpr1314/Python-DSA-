class Queue:
    def __init__(self):
        self.item = []
        self.front = None
        self.rear = None


    def is_empty(self):
        return len(self.item) == 0
    
    def enqueue(self, data):
        return self.item.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else: 
            raise IndexError('Queue is Empty')
        
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError('Queue is Empty')
        
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError('Stack is empty')
        
    def size(self):
        return len(self.item)
    

q = Queue()
q.enqueue(23)
q.enqueue(56)
q.enqueue(87)
q.enqueue(12)
q.dequeue()
print('size', q.size())
print('front', q.get_front())
print('rear', q.get_rear())


