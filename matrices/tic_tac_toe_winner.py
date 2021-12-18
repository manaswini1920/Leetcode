def tic_tac_toe_winner(moves):
    #3x3 grid
    n=3
    #rows,cols,diagonals
    row,col,d1,d2=[0]*n,[0]*n,0,0
    #first player =1 and second =-1
    player =1
    for r,c in moves:
        #first player put the first move
        row[r]+=player
        col[c]+=player

        #check if grids are filled
        #left to right diag
        if r==c:
            d1+=player
        if r+c==n-1:#right to left diag
            d2+=player
        #winning condition
        if abs(d1)==n or abs(d2)==n or abs(row[r])==n or abs(col[c])==n:
            if player==1:
                return 'A'
            else:
                return 'B'
    #give next player the chance
        player*=-1
    #still if we didnt find the winner

    #grids all are filled then
    if len(moves)==n*n:
        return "Draw"
    else:
        return "Pending"

print(tic_tac_toe_winner([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
