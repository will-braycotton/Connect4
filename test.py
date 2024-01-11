class Game:
    def __init__(self):
        self.board  = ["_"] * 9

    def print_board(self):
        print()
        for i in range(0,len(self.board),3):
            print(self.board[i+0], self.board[i+1], self.board[i+2])
        print()

    def is_win(self):
        #column
        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] !="_":
                print('column')
                return True, self.board[i]
        #row
        for i in range(0, len(self.board),3):
            if self.board[i+0] == self.board[i+1] == self.board[i+2] and self.board[i] !="_":
                print('row')
                return True, self.board[i]
        #diag 1 
        if (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != '_':
            print('diag 1')
            return True, self.board[0]
        if (self.board[2] == self.board[4] == self.board[6]) and self.board[2] != '_' :
            print('diag 2')
            return True, self.board[2]
        if self.blank_space() == 0:
            print('tie')
            return True, 0
        
        return False, 0
    
    def blank_space(self):
        return self.board.count("_")

    def move_piece(self, symbol,index):
        if self.board[index] != "_":
            return False
        else:
            self.board[index] = symbol
            self.print_board()
            return True
        
def print_board(board):
        print()
        for i in range(0,len(board),3):
            print(board[i+0], board[i+1], board[i+2])
        print()

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
            
def score(board,symbol):
    state,symbol_2 = board.is_win()
    if state and symbol == symbol_2:
        return 10
    elif state and symbol != symbol_2:
        return -10
    else:
        return 0
    
def generate_board_combos(board,symbol):
    all_list = []
    for index,value in enumerate(board):
        new_board= board.copy()
        if value =='_':
            new_board[index]= symbol
            all_list.append(new_board)
    
    if symbol == 'X':
        symbol = 'O'
    else:
        symbol='X'
    
    



def print_list_boards(list):
     for index,value in enumerate(list):
        print(index)
        print_board(value)

def minimax(board):
    #generate all possible board combinations
    '''If the game is over, return the score from X's perspective.
    Otherwise get a list of new game states for every possible move
    Create a scores list
    For each of these states add the minimax result of that state to the scores list
    If it's X's turn, return the maximum score from the scores list
    If it's O's turn, return the minimum score from the scores list'''


    pass
   
x = Game()
x.board = ['X','X','O','O','O','X', 'X','_','_']
#x.print_board()
generate_board_combos(x.board,'X')
w = True

'''
while w:
    prompt_user(x,'X','1')
    prompt_user(x,'O','2')

    state, symbol = x.is_win()

    if state:
        w = False

'''