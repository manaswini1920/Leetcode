class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
    def pop(self):
        return self.s1.pop()
    def peek(self):
        return self.s1[-1]
    def empty(self):
        return True if len(self.s1)==0 else False
    def print_val(self):
        if len(self.s1)!=0:
            print(self.s1)

q=Queue()
q.push(1)
q.push(2)
q.pop()
q.print_val()

