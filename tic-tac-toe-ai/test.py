import copy
import math

x = "X"
o = "O"
EMPTY =None

def initial_board():
    return [
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY]
    ]

def player(board):
    x_sum = 0
    o_sum = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == x:
                x_sum +=1
            elif board[i][j] == o:
                o_sum +=1
    
    return x if x_sum <= o_sum else o

def actions(board):
    empty_position = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY : 
                empty_position.add((i,j))
    return empty_position

def result(board,action):
    i,j = action
    empty_position = actions(board)
    player_played = player(board)
    if action in empty_position:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player_played
        return new_board
    else:
        raise ValueError ("invalid Value.")
    
def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0] 
           
    for i in range(3):
        if board[i][0] == board[i][1]==board[i][2] and board[i][0] is not None:
            return  board[i][0]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]   
    
    if board[0][2] == board[1][1] == board[2][0] and board[2][0] is not None:
           return board[2][0]

    return None

def terminal(board):
    if winner (board) is not None:
        return True
    elif not any(EMPTY in row for row in board):
        return True
    else:
        return False
    
def utility (board):
    if terminal(board):
        if winner(board) is not None:
            if winner(board) == x:
                return 1
            elif winner(board) == o:
                return -1
            
        else:
            return 0
    
    return None

def  minimax(board):
    if terminal(board):
        return None
    
    player_XorO = player(board)

    if player_XorO == x:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            move_score = min_value(result(board,action))
            if move_score > best_score:
                best_score = move_score
                best_move = action
        return best_move
    elif player_XorO == o:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            move_score = max_value(result(board,action))
            if move_score > best_score:
                best_score = move_score
                best_move = action
        return best_move

    

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max (v,min_value(result(board,action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min (v,max_value(result(board,action)))
    return v    