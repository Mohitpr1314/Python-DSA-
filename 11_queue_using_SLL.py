class Node:
    def __init__(self, item = None, next = None):
        self.item = item 
        self.next = next



class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.item_count = 0


    def is_empty(self):
        return self.front == None
    
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError('Queue is empty')
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('Queue is empty')
        
    def size(self):
        return self.item_count
    

q = Queue()
q.enqueue(23)
q.enqueue(56)
q.enqueue(87)
q.enqueue(12)
# q.dequeue()
print('size', q.size())
print('front', q.get_front())
print('rear', q.get_rear())

