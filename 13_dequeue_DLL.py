class Node:
    def __init__(self,item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
        


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0


    def insert_front(self, data):
        n = Node(data, None, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(data, self.rear, None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            self.front = self.front.next
            self.front.prev = None
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError('Dequeue is Empty')
        self.item_count -= 1
        
    def delete_rear(self):
        if not self.is_empty():
            self.rear = self.rear.prev
            self.rear.next = None
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError('Dequeue is empty')
        self.item_count -= 1
        
    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            return self.front.item
        

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            return self.rear.item
        

    def size(self):
        return self.item_count
        


d = Deque()


d.insert_front(4)
d.insert_front(23)
d.insert_rear(10)
d.insert_rear(46)
d.insert_rear(50)
# d.delete_front()
# d.delete_rear()
# d.delete_front()

print('size : ',d.size())
print('front', d.get_front())
print('rear', d.get_rear())