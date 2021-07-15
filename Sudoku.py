#Board to be solved. -1's represent empty squares
board = [
    [-1,-1,-1,-1,-1,5,-1,-1,4],
    [2,-1,8,-1,-1,-1,6,-1,9],
    [9,-1,5,4,2,-1,-1,-1,7],
    [-1,7,-1,-1,5,4,2,6,-1],
    [-1,-1,4,-1,6,-1,8,-1,-1],
    [-1,2,3,7,1,-1,-1,9,-1],
    [7,-1,-1,-1,4,3,9,-1,8],
    [3,-1,9,-1,-1,-1,5,-1,2],
    [4,-1,-1,5,-1,-1,-1,-1,-1]
]

#Array of 
e = []

#Function to print the board with the traditional Sudoku squares
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def __init__(self, b):
    board = b
    e = emptys()

def is_empty(bo, x,y):
    if (bo[x][y] == -1):
        return True
    return False

def exist(bo, val, x, y):
    row = 0
    col = 0
    if x < 3:
        row = 0
    elif x < 6:
        row = 3
    else:
        row = 6
    if y < 3:
        col = 0
    elif y < 6:
        col = 3
    else:
        col = 6
    for i in range(len(board)):
        if (bo[i][y] == val and i != x):
            return True
        if (bo[x][i] == val and i != y):
            return True
    for i in range(row,row+3):
        for j in range(col,col+3):
            if (bo[i][j] == val and i != x and j != y):
                return True
    return False

#Should function as described
def emptys(b):
    for i in range(len(b)):
        tmp = []
        for j in range(len(b[i])):
            if is_empty(b,i,j):
                tmp.append((i,j))
        e.append(tmp)
            
def find_next_empty(b):
    ret = (0,0)
    for i in range(len(b)):
        for j in range(len(b[i])):
            if (is_empty(b,i,j)):     # and (ret == (0,0))):
                ret = (i,j)
    return ret

#Should be recursive
def solve(b):
    (i,j) =  find_next_empty(b)
    if is_empty(b,i,j):
        for k in range(1,10):
            if not exist(b,k,i,j):
                b[i][j] = k
                if solve(b) == False:
                    b[i][j] = -1
                else:
                    return True
        return False
    else: 
        return True

print_board(board)
solve(board)
print("___________________")
print_board(board)
