class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self,root):
        self.root=Node(root)
        self.arr=[]
    def postorder(self,root):
        if root is None:
            return None
        self.postorder(root.left)
        self.postorder(root.right)
        self.arr.append(root.val)
        return self.arr
s=Solution(5)
s.root.left=Node(3)
s.root.right= Node(4)
s.root.left.left=Node(1)
s.root.left.right=Node(2)
print(s.postorder(s.root))
