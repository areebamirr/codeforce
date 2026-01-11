
# 10/01/2026. Took me 3 hours. Despite wrting whole code to print out seemingly correct result. Codefroce passed my code with 1/135 tests. Learned to code hard alot. Hardword 10/10. Smartwork 2/10. Improved more. It took me 4.5 hours to stick to this one problem

# # My solutions
# board = []
# for _ in range(3):
#     row = input().strip()
#     board.append(list(row))

# def win(board):
#     win = None
#     win_count = 0
#     for i in range(len(board)):
#         if (board[i] == board[i][0]*3) and (str(board[i][0]) != "."):
#             win = board[i][0]
#             win_count += 1
#     board = transpose(board)

#     for i in range(len(board)):
#         if (board[i] == board[i][0]*3) and (str(board[i][0]) != "."):
#             win = board[i][0]
#             win_count += 1    
#     board = transpose(board)

#     if win_count == 0:
#         if "".join(board[i][j] for i,j in [(0,0), (1,1), (2,2)]) == str(board[0][0]*3): win = board[0][0]; win_count += 1   # I got this help from internet resources
#         if "".join(board[i][j] for i,j in [(0,2), (1,1), (2,0)]) == str(board[0][2]*3): win = board[0][2]; win_count += 1    

#     if win_count > 1: return "illegal"
#     elif win_count == 1 and win == "X": return "the first player won"
#     elif win_count == 1 and win == "0": return "the second player won"
#     elif win_count == 0: return "draw"
#     else: return None

# def turns(board):
#     X_count = 0
#     Zero_count = 0
#     dot_count = 0
#     for i in board:
#         for j in i:
#             if "X" in j: X_count += 1
#             elif "0" in j: Zero_count += 1
#             elif "." in j: dot_count += 1

#     if dot_count >= 1:                                                #The conditional modification help by deepseek
#         if X_count == Zero_count + 1: return "second"
#         elif Zero_count == X_count + 1: return "first"
#     elif dot_count == 0:
#         if win(board) == "draw":
#             return "draw"

#     # if Zero_count == X_count: return "illegal"
#     if abs(X_count - Zero_count) > 1:
#         return "illegal"
#     else : return None

# def transpose(board):   # This must be understood before commiting to git. This one got help from online resources.
#     return [
#         "".join(board[j][i] for j in range(3))
#         for i in range(3)
#     ]

# layout_validity = True
# draw_possibility = False
# for i in board:
#     if len(i) == 3: layout_validity = True
#     else: layout_validity = False


# if layout_validity:
#     check_win = win(board)
#     if(check_win == None):
#         print(turns(board))
#     else:
#         print(check_win)
# else:
#     print("illegal")

# Deep seek soltions.
# Read the board
board = [input().strip() for _ in range(3)]

# Function to check if a player has won
def win(player, board):
    # Rows
    for row in board:
        if row == player * 3:
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Count X, 0, and empty cells
count_X = sum(row.count('X') for row in board)
count_0 = sum(row.count('0') for row in board)
count_empty = sum(row.count('.') for row in board)

# Who won?
X_won = win('X', board)
O_won = win('0', board)

# Validation and verdict logic
illegal = False

# First check for impossible counts
if count_0 > count_X or count_X - count_0 > 1:
    illegal = True
# If both players won simultaneously → illegal
elif X_won and O_won:
    illegal = True
# If X won, X must have one more than O
elif X_won and count_X != count_0 + 1:
    illegal = True
# If 0 won, counts must be equal
elif O_won and count_X != count_0:
    illegal = True

# Decide verdict
if illegal:
    print("illegal")
elif X_won:
    print("the first player won")
elif O_won:
    print("the second player won")
elif count_empty == 0:
    print("draw")
else:
    # Decide whose turn is next
    if count_X == count_0:
        print("first")
    else:
        print("second")