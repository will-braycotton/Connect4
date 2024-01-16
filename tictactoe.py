import random

class Newnode():
    count = 0
    def __init__(self):
        self.data = None
        self.number = Newnode.count
        self.parent = None
        self.depth = 0
        Newnode.count+=1
        
def move_piece(board, symbol,index):
    if board.data[index] != "_":
        return False
    else:
        board.data[index] = symbol
        print_board(board)
        return True
    
def blank_space(board):
        return board.count("_")

def print_board(board):
        print()
        for i in range(0,len(board.data),3):
            print(board.data[i+0], board.data[i+1], board.data[i+2])
        print()

def is_win(board):
        #column
        for i in range(0,3):
            if board.data[i] == board.data[i+3] == board.data[i+6] and board.data[i] !="_":
                return True, board.data[i]
        #row
        for i in range(0, len(board.data),3):
            if board.data[i+0] == board.data[i+1] == board.data[i+2] and board.data[i] !="_":
                return True, board.data[i]
        #diag 1 
        if (board.data[0] == board.data[4] == board.data[8]) and board.data[0] != '_':
            return True, board.data[0]
        if (board.data[2] == board.data[4] == board.data[6]) and board.data[2] != '_' :
            return True, board.data[2]
        if blank_space(board.data) == 0:
            return True, 0
        
        return False, 0

def prompt_user(board, symbol,player):
    while True:
        try:
            user_input=int(input(f'Player {player} select space 0-8: '))
            if move_piece(board,symbol,user_input):
                return True
            else:
                print('Error space already occupied!')
        except:
            print('Enter a integer')
   
def node_depth(node):
    counter =0
    while node.parent != None:
        counter+=1
        node = node.parent

    return counter

def generate_board_combos(board_node,symbol,main_list, end_list):
    board = board_node.data
    for index,value in enumerate(board):
        if value == '_':
            new_board = Newnode()
            new_board.parent = board_node
            new_board.data = board.copy()
            new_board.data[index]= symbol
            main_list.append(new_board)
            new_board.depth = node_depth(new_board)
            value,x = is_win(new_board)
            if '_' in new_board.data and not value:
                symbol ='X' if symbol =='O' else 'O'
                generate_board_combos(new_board,symbol,main_list,end_list)
                minimax
            else:
                end_list.append(new_board)
                
            
         
def score(game_states,scores_list,symbol):
    for board in game_states:
        state,symbol_2 = is_win(board)
        if state and symbol == symbol_2:
            scores_list.append(20 - board.depth) 
        elif state and symbol != symbol_2 and symbol_2 != 0:
            scores_list.append(-20 + board.depth)
        else:
            scores_list.append(0 + board.depth)

def parent(board):
    while board.parent.parent != None:
        board = board.parent
    return board   

def move_difference(board):
    parent = board.parent.data
    for index, value in enumerate(parent):
        if board.data[index] != value:
            return index
        
def minimax(board,symbol):
    game_states = []
    end_list=[]
    generate_board_combos(board,symbol,game_states,end_list)

    scores_list =[]
    score(end_list,scores_list,symbol)
    
    index  = scores_list.index(max(scores_list))
    best_node_move  = end_list[index]
    
    print(scores_list)
    print(index)
    print(best_node_move.data)

    move  = parent(best_node_move)
    best_move  = move_difference(move)
    return best_move

def menu():
    MENU = '\nWelcome to Tic-Tac-Toe!\nSelect a mode from below:\n\n1. User vs Random AI\n2. User vs Minimax AI\n3. Minimax AI vs Random AI\n4. Minimax AI vs Minimax AI \n5. Quit\n\nEnter your selection:'
    user_input = input(MENU)
    while not(user_input =='1' or user_input =='2' or user_input =='3' or user_input =='4' or user_input == '5'):
        print('Enter Valid Menu Input')
    return user_input

def rand(board):
    x= True
    while x:
        index = random.randint(0,8)
        if board.data[index] == '_':
            move_piece(board,'O', index)
            return


user_input = menu()
while user_input != '5':
    board = Newnode()
    board.data = ["_"] * 9
    print_board(board)

    if user_input == '1':
        w =True
        while w:
            prompt_user(board,'X','1')
            state, symbol = is_win(board)
            if not state:
                rand(board)

            state, symbol = is_win(board)

            if state:
                w = False
                if symbol == 0:
                    print('Its a tie!')
                else:
                    print(f'{symbol} Won!')

    if user_input == '2':
        w =True
        while w:
            prompt_user(board,'X','1')
            state, symbol = is_win(board)
            if not state:
                move_piece(board,'O',minimax(board,'O'))

            state, symbol = is_win(board)

            if state:
                w = False
                if symbol == 0:
                    print('Its a tie!')
                else:
                    print(f'{symbol} Won!')

    if user_input == '3':
        w =True
        while w:
            move_piece(board,'X',minimax(board,'X'))
            state, symbol = is_win(board)
            if not state:
                rand(board)

            state, symbol = is_win(board)

            if state:
                w = False
                if symbol == 0:
                    print('Its a tie!')
                else:
                    print(f'{symbol} Won!')

    if user_input == '4':
        w =True
        while w:
            move_piece(board,'X',minimax(board,'X'))
            state, symbol = is_win(board)
            if not state:
                move_piece(board,'O',minimax(board,'O'))

            state, symbol = is_win(board)

            if state:
                w = False
                if symbol == 0:
                    print('Its a tie!')
                else:
                    print(f'{symbol} Won!')

    if not user_input =='5':
        user_input= input('Would you like to play again? (y/n)')
        if user_input == 'y':
            user_input = menu()
        else:
            user_input = '5'


#need to account for the other player picking the best move as well