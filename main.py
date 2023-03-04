# I want to give credit to this website for helping me figure out  
# the logic for determining the winner of the game
# https://www.askpython.com/python/examples/connect-four-game

def create_board(rows, cols):
    # Creating a 6x6 board being used for Connect-4
    board = []
    for row in range(rows):
        board.append([])
        for col in range(cols):
            board[row].append('-')
    return board

def print_board(board):
   # Print the current game board
    for row in board:
        print('|', end='')
        for val in row:
            print(val + '|', end='')
        print()
    print('--------------')

def get_move(player, board):
    #Get the player's move and update the board
    col = int(input(f'Player {player}, enter column (0-{len(board[0])-1}): '))
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == '-':
            board[row][col] = player
            return True
    return False

def check_winner(board, player):
    #Check if the current player has won
	
    # Checking to see if the row has four in a row 
    for row in range(len(board)):
        for col in range(len(board[0])-3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Checking columns to see if the column has four in a row 
    for row in range(len(board)-3):
        for col in range(len(board[0])):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    
	# Check diagonals to see if it's four in a row (top left to bottom right)
    for row in range(len(board)-3):
        for col in range(len(board[0])-3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    
	# Check diagonals to see if it's four in a row (bottom left to top right)
    for row in range(3, len(board)):
        for col in range(len(board[0])-3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    return False

def play_game():
    """Play Connect 4 game"""
    rows = 6
    cols = 6
    board = create_board(rows, cols)
    print_board(board)

    # Loop until a player wins or the board is full
    player = 'X'
    while True:
        if not get_move(player, board):
            print(f'Column is full, try again player {player}!')
            continue

        print_board(board)

        if check_winner(board, player):
            print(f'Player {player} wins!')
            break

        # Checking for a draw
        if all([val != '-' for row in board for val in row]):
            print('It\'s a draw!')
            break

        # Switch player turns 
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

play_game()
