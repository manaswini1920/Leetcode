from collections import deque
class Stack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
        return self.q
    def pop(self):
        for i in range(len(self.q)-1):#except the last element
            self.q.append(self.q.popleft())
        return self.q.popleft()
    def top(self):
        return self.q[-1]
    def empty(self):
        return len(self.q)==0

s=Stack()
s.push(1)
print(s.push(2))
print(s.pop())
s.pop()
print(s.empty())