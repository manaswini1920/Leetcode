class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self,root):
        self.arr=[]
        self.root=Node(root)
    def preorder(self,root):
        if root is None:
            return None
        self.arr.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.arr

s=Solution(2)
s.root.left=Node(1)
s.root.right=Node(3)
print(s.preorder(s.root))
