class prioQue:
    
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    

    def push(self, data, priority):
        index= 0
        while index < len(self.item) and self.items[index][1]:
            index += 1
        self.item.insert(index, (data, priority))
    
    def pop(self, index):
        if not self.is_empty():
            return self.item.pop(0)[0]
        else:
            raise IndexError('Queue is empty')
        

    def size(self):
        return len(self.item)
    

q = prioQue()
q.push()