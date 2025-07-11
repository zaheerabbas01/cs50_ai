"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_len = sum(row.count(X) for row in board)
    o_len = sum(row.count(O) for row in board)

    if x_len == 0 or x_len == o_len:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                act.add((i,j))

    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board =copy.deepcopy(board)
    if action is None or action[0] > 3 or action[0] < 0 or action[1] > 3 or action[1] < 0:
        raise ValueError("Invalid Action")

    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid Action")
    else:
        new_board[action[0]][action[1]] = player(board)
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    w = player(board)
    if w == X:
        w = O
    else:
        w = X
    #check horizontally
    if [w,w,w] in board:
        return w
    
    #check vertically
    for i in range(3):
        if w == board[0][i] and w == board[1][i] and w == board[2][i]:
            return w

    #check diagnolly
    if w == board[0][0] and w == board[1][1] and w == board[2][2]:
        return w
     
    if w == board[0][2] and w == board[1][1] and w == board[2][0]:
        return w
  
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    x = True
    for i in board:
        if EMPTY in i:
            x =  False
    
    if winner(board) is None and not x:
        return False
    
    if winner(board) != None:
        return True
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w is X:
        return 1
    elif w is O:
        return -1
    else:
        return 0
    
def max_value(s):
    v = -math.inf
    if terminal(s):
        return utility(s)
    for a in actions(s):
        v = max(v,min_value(result(s,a)))
    return v
    
def min_value(s):
    v = math.inf
    if terminal(s):
        return utility(s)
    for a in actions(s):
        v = min(v,max_value(result(s,a)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    pl = player(board)
    p = 1
    k = 1
    p1 = -1
    k1 = -1

    for a in actions(board):
        max_player = min_value(result(board,a))
        min_player = max_value(result(board,a))
        
        if max_player <= p and min_player <= k and pl is O:
            p = max_player
            k = min_player
            r = a
        elif min_player >= p1 and max_player >= k1 and pl is X:
            p1 = min_player
            k1 = max_player
            r = a
    return r
