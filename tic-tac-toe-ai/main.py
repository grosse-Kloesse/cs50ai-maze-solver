import math
from tictactoe import player,actions,result,terminal,utility,initial_state,winner

def minimax(board):
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == "X":
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            move_score = min_value(result(board,action),-math.inf,math.inf)
            if move_score > best_score:
                best_score = move_score
                best_action = action
        return best_action
    
    elif current_player == "O":
        best_score = math.inf
        best_action = None
        for action in actions(board):
            move_score = max_value(result(board,action),-math.inf,math.inf) 
            if move_score < best_score:
                best_score = move_score
                best_action = action
        return best_action
    

def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,min_value(result(board,action),alpha,beta))
        alpha = max (alpha,v)
        if beta <= alpha:
            break
    return v 

def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action),alpha,beta))
        beta = min (beta,v)
        if alpha >= beta:
            break

    return v

