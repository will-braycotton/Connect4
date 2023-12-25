def create_board():
    board = []
    for i in range(0,6):
        board.append(["_"]*7 )
    return board

def print_board(board):
    for i in board:
        for x in i:
            print(x, end=' ')
        print()
    for i in range(0,7):
        print(i, end=" ")
    print()
    print()

def move_piece(column, symbol, board):
    for i in range(5,-1, -1):
        if board[i][column] == '_':
            board[i][column] = symbol
            print_board(board)
            return 

def is_win(board):
    #same row
    for row in board:
        count = 1
        previous = "_"
        for value in row:
            if value == previous and value != "_":
                count+=1
                if count == 4:
                    if value == "X":
                        return True, "Player 1 Wins!"
                    else:
                        return True, "Player 2 Wins!"
            else:
                count =1 
            previous = value
    #column
    for column in range(0,7):
        count = 1
        previous = "_"
        for row in range(0,6):
            current = board[row][column]
            if current == previous and current != "_":
                count+=1
                if count == 4:
                    if current == "X":
                        return True, "Player 1 Wins!"
                    else:
                        return True, "Player 2 Wins!"
            else:
                count =1 
            previous = current
    #Diagonal 
    for row in range(0,6):
        for column in range(0,7):
            previous = '_'
            for n in range(0,7):
                try:
                    current = board[row + n][column + n]
                except:
                    n=8
                    count = 1
                    current='_'
                if current == previous and current != "_":
                    count+=1
                    if count == 4:
                        if current == "X":
                            return True, "Player 1 Wins!"
                        else:
                            return True, "Player 2 Wins!"
                else:
                    count =1 
                previous = current
    for row in range(0,6):
        for column in range(0,7):
            previous = '_'
            for n in range(0,7):
                try:
                    current = board[row - n][column + n]
                except:
                    n=8
                    count = 1
                    current='_'
                if current == previous and current != "_":
                    count+=1
                    if count == 4:
                        if current == "X":
                            return True, "Player 1 Wins!"
                        else:
                            return True, "Player 2 Wins!"
                else:
                    count =1 
                previous = current
    return False, "Its a tie"

def user_input_():
    user_input = input(menu)
    while True:
        if user_input == "X" or user_input == "1" or user_input == "2":
            return user_input
        user_input = input('Error, Enter a valid input! \n')

def valid_player_input(player):

    while True:
        try: 
            player_input = int(input(f'Player {player} select a column: \n'))
            if player_input in [0,1,2,3,4,5,6]:
                return player_input
            else:
                print('Error, enter a valid number between 0 and 6')
        except:
            print("Error, Enter a numerical value")
            player_input = "n/a"
    

menu = 'Welcome to Connect Four\n1: Single Player\n2: Two Player\nX: Exit\n'
user_input = user_input_()

while user_input != "X":
    board = create_board()       
    if user_input == "2":
        win = False
        while win ==  False:
            print_board(board)

            player_1_input = valid_player_input("1")
            move_piece(player_1_input, "X",board)
            win, winner = is_win(board)
            if win == False:
                player_2_input = valid_player_input("2")
                move_piece(player_2_input, "O",board)


            win, winner = is_win(board)
        print(winner)
    
    user_input = user_input_()
