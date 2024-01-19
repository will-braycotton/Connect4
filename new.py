

def minimax(board, depth):
    
    if terminal(board)[0]:
        return score(board, depth), 0

    depth+=1
    if player_turn(board) == 'X':
        value = (-99,0)
        for a in action(board):
            value = (max(value[0], minimax(result(board,a), depth)[0]),a)
            #print(f'{value}, {a} , {depth}')
            
        return value
    
    if player_turn(board) == 'O':
        value = (99,0)
        for a in action(board):
            value = (min(value[0], minimax(result(board,a), depth)[0]),a)
            #print(f'{value}, {a} , {depth}')
        return value


def terminal(board):
    #returns bool expersion for state of the game
        for i in range(0,3):
            if board[i] == board[i+3] == board[i+6] and board[i] !="_":
                return True, board[i]
        for i in range(0, len(board),3):
            if board[i+0] == board[i+1] == board[i+2] and board[i] !="_":
                return True, board[i]
        if (board[0] == board[4] == board[8]) and board[0] != '_':
            return True, board[0]
        if (board[2] == board[4] == board[6]) and board[2] != '_' :
            return True, board[2]
        if not '_' in board:
            return True, 0
        
        return False, 0
    

def score(board, depth):
    #returns score of the board
    if terminal(board)[1] == 'X':
        return 10 - depth
    if terminal(board)[1] == 'O':
        return depth - 10
    return 0

def player_turn(board):
    #returns whos players turn it is
    if board.count('X') > board.count('O'):
        return 'O'
    return 'X'

def result(board, new_move):
    #returns what the new_board terminal state will be
    new_board = board.copy()
    new_board[new_move] = player_turn(board)
    return new_board

def action(board):
    #returns all of the possible moves for a given board
    actionlist=[]
    for index, value in enumerate(board):
        if value == '_':
            actionlist.append(index)
    return actionlist


def print_board(board):
        print()
        for i in range(0,len(board),3):
            print(board[i+0], board[i+1], board[i+2])
        print()

def best_next_move(board):
    actionlist = action(board)
    for a in actionlist:
        pass
board = ['_','_','_','_','_','_','_','_','_']

print_board(board)
print(minimax(board, 0))
print('hello')

while not terminal(board)[0]:
    best_move  = minimax(board,0)[1]
    board[best_move] = 'X'
    print(f'Best move: {best_move}')
    print_board(board)
    if not terminal(board)[0]:
        user_input = int(input('Enter a index:'))
        board[user_input] = 'O'
        print_board(board)

print(terminal(board)[1])

#test