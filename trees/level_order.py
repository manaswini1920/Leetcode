import collections


class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def levelorder(self,root):
        if root is None:
            return None
        output=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            level=[]
            for _ in range(len(queue)):
                root=queue.popleft()
                if root:
                    level.append(root.val)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
            output.append(level)
        return output
s=Solution()
s.root=Node(2)
s.root.left=Node(1)
s.root.right=Node(3)
s.root.left.left=Node(4)
s.root.left.right=Node(5)
print(s.levelorder(s.root))
