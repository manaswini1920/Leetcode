def height(root):
    if not root:
        return -1
    return 1+max(height(root.left),height(root.right))
def balanced_binary_tree(root):
    if not root:
        return True
    return abs(height(root.right)-height(root.left))<2 and \
           balanced_binary_tree(root.left) and balanced_binary_tree(root.right)
