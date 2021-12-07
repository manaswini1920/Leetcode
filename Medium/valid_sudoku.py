def valid_sudoku(board):
    #row
    N=9 #9x9 matrix
    for r in range(N):
        row=[c for c in board[r] if c!='.']
        if len(row)!=len(set(row)):
            return False
    #col
    for c in range(N):
        col = [board[r][c] for r in range(N) if board[r][c]!='.']
        if len(col)!=len(set(col)):
            return False
    #subbox
    def helper(r,c):
        l=set()
        for R in range(r,r+3):
            for C in range(c,c+3):
                if board[r][c]=='.':
                    continue
                if board[r][c] not in l:
                    l.add(board[r][c])
                else:
                    return False
        return True

    for i in range(0,N,3):
        for j in range(0,N,3):
            if not helper(i,j):
                return False
    return True


print(valid_sudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))