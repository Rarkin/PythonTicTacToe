import random

def draw_board(board):
    # This function prints out the board that it was passed.
    # board is a list of 10 strings representing the board ignore index 0 for simplicity sake
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    # Let's the player type which letter they want to be then returns a list with player letter first, computers second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def pick_first_player():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def check_for_winner(board, letter):
    # check for matching letters for winner
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def copy_board(board):
    # Make a cpoy of the board and return it
    copyofboard = []

    for i in board:
        copyofboard.append(i)

    return copyofboard

def check_space_available(board, move):
    # Return true if the passed move can be done
    return board[move] == ' '

def player_move(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_space_available(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def random_move(board, movesList):
    # Returns a valid move from passed list otherwise return false
    possibleMoves = []
    for i in movesList:
        if check_space_available(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computer_move(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # check if computer can win
    for i in range(1, 10):
        copy = copy_board(board)
        if check_space_available(copy, i):
            make_move(copy, computerLetter, i)
            if check_for_winner(copy, computerLetter):
                return i
    
    # Check if player can win and block them.
    for i in range(1, 10):
        copy = copy_board(board)
        if check_space_available(copy, i):
            make_move(copy, playerLetter, i)
            if check_for_winner(copy, playerLetter):
                return i

    # take one of the corners if possible
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # take the center if possible
    if check_space_available(board, 5):
        return 5

    # Move on side
    return random_move(board, [2, 4, 6, 8])

def check_board_full(board):
    # Return True if board is full otherwise retuen false
    for i in range(1, 10):
        if check_space_available(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = input_player_letter()
    turn = pick_first_player()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            draw_board(theBoard)
            move = player_move(theBoard)
            make_move(theBoard, playerLetter, move)

            if check_for_winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if check_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)

            if check_for_winner(theBoard, computerLetter):
                draw_board(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if check_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break