
class Stack:
    stackList = []
    
    def __init__(self, var = []):
        self.stackList = list(var)
    
    def push(self, var):
        self.stackList = [var] + self.stackList

    def pop(self): 
      self.stackList = self.stackList[1:]
    
    def print(self):
        print(self.stackList)

stack = Stack([100, 2, 50, 1]) 
stack.push(200) 
stack.print()

stack.pop()
stack.print()
