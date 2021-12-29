def same_tree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val !=q.val:
        return False
    return same_tree(p.right,q.right) and same_tree(p.left,q.left)
