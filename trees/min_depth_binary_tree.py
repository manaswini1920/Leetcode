def min_depth_binary_tree(root):
    if root is None:
        return 0
    else:
        stack=[(1,root)]
        min_depth=float('inf')
        while stack:
            depth,root=stack.pop()
            children=[root.left,root.right]
            if not any(children):
                min_depth=min(min_depth,depth)
            for c in children:
                if c:
                    stack.append((depth+1,c))
    return min_depth
