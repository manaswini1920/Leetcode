def reshape_matrix(mat,r,c):
    m=len(mat)
    n=len(mat[0])
    if r*c!=m*n:
        return mat
    output =[[0 for _ in range(c)]for _ in range(r)]
    k=0
    for i in range(m):
        for j in range(n):
            output[k//c][k%c]=mat[i][j]
            k+=1
    return output
print(reshape_matrix( [[1,2],[3,4]],1,  4))
