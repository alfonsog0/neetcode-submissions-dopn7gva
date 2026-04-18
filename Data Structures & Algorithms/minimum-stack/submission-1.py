class MinStack: 
    """
    # naive O(n) getMin()
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]
    """
    # minStack keeps track of the minimum
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]
