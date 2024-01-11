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
            


x = Game()
x.print_board()
w = True
while w:
    prompt_user(x,'X','1')
    prompt_user(x,'O','2')

    state, symbol = x.is_win()

    if state:
        w = False

