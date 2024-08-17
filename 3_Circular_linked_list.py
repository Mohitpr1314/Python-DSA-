class Node:
    def __init__(self, item = None, next=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def insert_at_first(self, data):
        n= Node(data,self.last.next)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            self.last.next = n


    def insert_at_last(self, data):
        n = Node(data,self.last.next)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def search(self, data):
        if not self.is_empty():
            temp = self.last.next
            while temp is not self.last:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
            return None
        
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp ==self.last:
                self.last = n

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp is not self.last:
                print(temp.item, end=' ')
                temp = temp.next
                break
            print(temp.item)
            
        
            

    def delete_frist(self):
        if not self.is_empty():
            if self.last.next == self.last:
                return None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                return None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp




myList = CLL()
myList.insert_at_first(5)
myList.insert_at_first(8)
myList.print_list()
print()




                

