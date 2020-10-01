class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def push(self,item):
        self.items.append(item)  # adding the item in items 

    def pop(self):
        return self.items.pop()  #deleting the item on top

    def peek(self):
        return self.items[len(self.items)-1]   #returning tos (top of stack)

    def size(self):
        return len(self.items)    #returning the size of stack
stack.push(5)
stack.push(6)
stack.push(7)

stack.size()
#output  :: 3
#item is now [5,6,7]
stack.is_empty()
#output  :: [5,6,7]
stack.pop()
#output :: [5,6]
stack.peek()
#output :: 6
