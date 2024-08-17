class Node:
    
    
    
    def __init__(self,prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start= None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        while temp is not None:
            temp = temp.next

        n = Node(temp , data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n


    def print_mylist(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next


    def delete_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    break
                temp = temp.next
    def __iter__(self):
        return DLLIterator(self.start)


class DLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data





        




# Driven code
start_node = Node()  # Create a start node
myList = DLL(start_node)  # Pass the start node to the DLL constructor

myList.insert_at_first(3)
myList.insert_at_first(5)
myList.insert_at_first(9)
myList.delete_last()

myList.print_mylist()  # Print the elements of the doubly linked list
print()
