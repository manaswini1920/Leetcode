import collections


class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def max_depth(self,root,depth):
        if root:
            l=self.max_depth(root.left,depth+1)
            r=self.max_depth(root.right,depth+1)
            return max(l,r)
        else:
            return depth






s=Solution()
s.root=Node(2)
s.root.left=Node(1)
s.root.right=Node(3)
s.root.left.left=Node(4)
s.root.left.right=Node(5)
print(s.max_depth(s.root,0))
