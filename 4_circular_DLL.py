class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev 
        self.next = next


class CDLL:
        def  __init__(self, start = None):
            self.start = start

        def is_empty(self):
            return self.start == None
        
        def insent_at_first(self, data):
            n = Node(data)
            if self.is_empty():
                n.next = n
                n.prev = n

            else:
                n.next = self.start
                n.prev = self.start.prev
                self.start.prev.next = n 
                self.start.prev = n
            self.start = n


        def insert_at_last(self, data):
            n = Node(data)
            if self.is_empty():
                n.next = n
                n.prev = n

            else:
                n.next = self.start
                n.prev = self.start.prev
                n.prev.next =n
                self.start.prev = n

        def search(self, data):
            temp = self.start
            if temp.item == data:
                return temp
            if temp == None:
                return None
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.item == data:
                        return temp
                    temp = temp.next

                return None
            

        def insert_after(self, temp, data):
            if temp is not None:
                n = Node(data)
                n.next = temp.next
                n.prev = temp
                temp.next.prev = n
                temp.next = n

        def print_list(self):
            temp = self.start
            if temp is not None:
                print(temp.item, end = '')
                temp = temp.next
                while temp is not self.start:
                    print(temp.item, end = ' ')
                    temp = temp.next



        def selete_first(self):
            if self.start is not None:
                if self.start.next == self.start:
                    self.start = None

                else:
                    self.start.prev.next = self.start.next
                    self.start.next.prev = self.start.prev
                    self.start = self.start.next

        def delete_last(self):
            if self.start is not None:
                if self.start.next == self.start:
                    self.start = None

                else:
                    self.start.prev.prev.next = self.start
                    self.start.prev = self.start.prev.prev



        def delete_item(self,data):
            if self.start is not None:
                temp = self.start
                if temp.item == data:
                    self.delete_first()

                else:
                    temp = temp.next 
                    while temp is not self.start:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next


# st = Node()
myList = CDLL()
myList.insent_at_first(34)
myList.insent_at_first(56)
myList.insent_at_first(23)
myList.insent_at_first(65)
myList.insent_at_first(87)
myList.insent_at_first(8)
myList.insert_at_last(56)
myList.insent_at_first(23)
myList.print_list()

