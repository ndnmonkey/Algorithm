class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[len(self.items)-1]
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
    def push(self,i):
        return self.items.append(i)
    def prin(self):
        print(self.items)
        return self.items
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    s.prin()