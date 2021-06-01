'''
This problem is to find an arrangement of N queens on a chess board, such that no queen can attack any other queens on the board.
The chess queens can attack in any direction as horizontal, vertical, horizontal and diagonal way.
A matrix is used to display the positions of N Queens, where no queens can attack other queens.
'''
N = int(input("enter Number of rows :"))
'''
printing the solution
'''
def Solution(game):
    for i in range(N):
        for j in range(N):
            print(game[i][j], end=" ")
        print()

'''
checking towards left,upper and lower diagonal whether any other Queen is present.
'''
def check(game, row, col):
    for i in range(col):
        if game[row][i] == "Q":
            return 0
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if game[i][j] == "Q":
            return 0
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if game[i][j] == "Q":
            return 0
    return 1

'''
backtracking algorithm is used to place the Queen at right place
'''
def solve(game, col):
    if col >= N:
        return 1
    for i in range(N):
        if check(game, i, col):
            game[i][col] = "Q"
            if solve(game, col + 1):
                return 1
            game[i][col] = "_"
    return 0


'''
includes intialisation and printing the solution
'''
def main():
    game = []
    for i in range(N):
        game.append(["_" for j in range(N)])
    if solve(game, 0) == 0:
        print("Solution does not exist")
        return False
    Solution(game)
    return True


main()
'''
Sample I/O and O/P
5
Q _ _ _ _ 
_ _ _ Q _ 
_ Q _ _ _ 
_ _ _ _ Q 
_ _ Q _ _


TIME COMPLEXITY OF N-QUEEN PROBLEM IS O(N!)
SPACE COMPLEXITY OF N-QUEEN PROBLEM IS O(N)
'''
