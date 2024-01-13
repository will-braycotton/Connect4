class Game:
    def __init__(self):
        self.board  = ["_"] * 9
    
    
    def move_piece(self, symbol,index):
        if self.board[index] != "_":
            return False
        else:
            self.board[index] = symbol
            self.print_board()
            return True
def blank_space(board):
        return board.count("_")

def print_board(board):
        print()
        print(board.number, board.parent.number, board.depth)
        for i in range(0,len(board.data),3):
            print(board.data[i+0], board.data[i+1], board.data[i+2])
        print()

def is_win(board):
        #column
        for i in range(0,3):
            if board[i] == board[i+3] == board[i+6] and board[i] !="_":
                return True, board[i]
        #row
        for i in range(0, len(board),3):
            if board[i+0] == board[i+1] == board[i+2] and board[i] !="_":
                return True, board[i]
        #diag 1 
        if (board[0] == board[4] == board[8]) and board[0] != '_':
            return True, board[0]
        if (board[2] == board[4] == board[6]) and board[2] != '_' :
            return True, board[2]
        if blank_space(board) == 0:
            return True, 0
        
        return False, 0
class Newnode():
    count = 0
    def __init__(self):
        self.data = None
        self.number = Newnode.count
        self.parent = None
        self.depth = 0
        Newnode.count+=1

def prompt_user(board, symbol,player):
    while True:
        try:
            user_input=int(input(f'Player {player} select space 0-9: '))
            if x.move_piece(symbol,user_input):
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
            value,x = is_win(new_board.data)
            if '_' in new_board.data and not value:
                symbol ='X' if symbol =='O' else 'O'
                x = generate_board_combos(new_board,symbol,main_list,end_list)
            else:
                end_list.append(new_board)
                
            
         
def score(game_states,scores_list,symbol):
    for board in game_states:
        state,symbol_2 = is_win(board.data)
        if state and symbol == symbol_2:
            scores_list.append(20 - board.depth) 
        elif state and symbol != symbol_2 and symbol_2 != 0:
            scores_list.append(-20 + board.depth)
        else:
            scores_list.append(0 + board.depth)
    

def minimax(board,symbol):
    #generate all possible board combinations
    '''If the game is over, return the score from X's perspective.
    Otherwise get a list of new game states for every possible move
    Create a scores list
    For each of these states add the minimax result of that state to the scores list
    If it's X's turn, return the maximum score from the scores list
    If it's O's turn, return the minimum score from the scores list'''

    game_states = []
    end_list=[]
    generate_board_combos(board,symbol,game_states,end_list)

    scores_list =[]
    score(end_list,scores_list,symbol)

    print(scores_list)
    print(len(scores_list))
    
    '''index  = scores_list.index(max(scores_list))
    print(index)'''

    pass




board = Newnode()

board.data = ['X','O','O','_','_','X','_','_','_']

my_list = []
end_list=[]
generate_board_combos(board,'X',my_list,end_list)



for node in end_list:
    print_board(node)

minimax(board,'X') 




'''
x = Game()
x.print_board()
w = True
while w:
    prompt_user(x,'X','1')
    prompt_user(x,'O','2')

    state, symbol = x.is_win()

    if state:
        w = False
'''
