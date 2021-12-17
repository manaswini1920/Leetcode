class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self,root):
        self.arr=[]
        self.root=Node(root)
    def inorder(self,root):
        if root is None:
            return None
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        return self.arr

s=Solution(2)
s.root.left=Node(1)
s.root.right=Node(3)
print(s.inorder(s.root))
