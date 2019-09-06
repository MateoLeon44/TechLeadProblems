class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []


    def push(self,val):
        self.stack.append(val)
        if not self.maxStack: 
            self.maxStack.append(val)
        elif val > self.maxStack[-1]:
            self.maxStack.append(val)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        self.maxStack.pop()
        return self.stack.pop()

    
    def max(self):
        return self.maxStack[-1]
        # Fill this in.
        
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(30)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2