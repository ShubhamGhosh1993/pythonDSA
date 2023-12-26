class MyStack:
    def __init__(self) -> None:
        self.items = []
        pass
    
    def push(self, item)-> None:
        self.items.append(item)
    
    def pop(self)-> None:
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
    
    def top(self)-> None:
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Top from an empty stack")
    
    def isEmpty(self)-> None:
        return len(self.items) == 0
    
    def size(self)-> None:
        return len(self.items)
      
s1 = MyStack()
print(type(s1))
s1.push(1)
s1.push(2)
print(s1.top())
print(s1.pop())
print(s1.pop())
print(s1.top())