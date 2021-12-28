def set_matrix_zero(matrix):
    def make_row_zero(matrix,i,j):
        if j<len(matrix[0]):
            matrix[i][j]=0
            return make_row_zero(matrix,i,j+1)
        return matrix
    def make_col_zero(matrix,i,j):
        if i<len(matrix):
            matrix[i][j]=0
            return make_col_zero(matrix,i+1,j)
        return matrix
    l=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                l.append((i,j))
    for i,j in l:
        make_row_zero(matrix,i,0)
        make_col_zero(matrix,0,j)
    return matrix
print(set_matrix_zero([[1,1,1],[1,0,1],[1,1,1]]))