#print all the possible ways to place the queen such that it must not collide........

def printPaths(n):
    board=[[0 for j in range(n)]for i in range(n)]
    printPathsHelper(0,n, board)

def printPathsHelper(row, n, board):
    if row ==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
        print()
        return
    
    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col]=1
            printPathsHelper(row+1, n, board)
            board[row][col]=0
    return

def isSafe(row, col, board, n):
    #vertical direction
    


n= int(input())
printPaths(n)