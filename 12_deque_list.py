class Deque:
    def __init__(self):
        self.item = []
        self.front = None
        self.rear = None

    def is_empty(self):
        return len(self.item) == 0

    
    def insert_front(self, data):
        return self.item.insert(0, data)
        

    def insert_rear(self, data):
        return self.item.append(data)
        

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            self.item.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            self.item.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            return self.item[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        else:
            return self.item[-1]

    def size(self):
        return len(self.item)


d = Deque()
d.insert_front(4)
d.insert_front(7)
d.insert_rear(10)
d.insert_rear(46)
print('size : ',d.size())
print('front', d.get_front())
print('rear', d.get_rear())




