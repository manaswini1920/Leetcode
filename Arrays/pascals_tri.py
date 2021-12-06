def pascal_tri(numrows):
    res=[[1]*(i+1) for i in range(numrows)]
    for r in range(numrows):
        for c in range(1,r):
            res[r][c]=res[r-1][c-1]+res[r-1][c]
    return res
print(pascal_tri(5))