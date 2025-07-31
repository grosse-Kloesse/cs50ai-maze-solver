import copy

"""
Tic Tac Toe AI using Minimax
"""

x = "X"
o = "O"
EMPTY = None

def  initial_state():
    """
    Returns starting state of the board: 3x3 frid of all EMPTY
    """
    return [
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY]
    ]

def player(board):
    """
    Returns player who has the next turn on a board.
    X always goes first.
    """
    x_count = sum(row.count(x) for row in board)
    o_count = sum(row.count(o) for row in board)
    return x if x_count <= o_count else o

def actions(board):
    empty_position = set()
    empty_position.update((i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY  )
    
    return empty_position

def result(board,action):
    
    empty_position = actions(board)
    player_play = player(board)
    if action in empty_position:
        i,j = action
        new_board = copy.deepcopy(board)
        new_board[i][j] = player_play
    else:
        raise ValueError("Invalid action: position already taken.")
    return new_board

def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal (board):
    if winner(board) is not None :
        return True
    elif not any (None in row for row in board):
        return True
    else:
        return False 

def utility(board):
    if terminal(board):
        if winner(board) ==x:
            return 1
        elif winner(board) == o:
            return -1
        else:
            return 0 



if __name__ == "__main__":
    print(terminal(initial_state()))
    
