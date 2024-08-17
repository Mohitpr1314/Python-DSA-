class Stack:

    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    
    def push(self, data):
        return self.item.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError('Stack is Empty')
        
    def size(self):
        return len(self.item)
    


    

st = Stack()
st.push(4)
st.push(7)
st.push(5)
st.push(7)
st.push(4)
print()
st.is_empty()
print()






# st.pop()
# print('the peek item', st.peek)






# for item in reversed(st.item):
#     print('the peek item', st.peek)
#     print(item)