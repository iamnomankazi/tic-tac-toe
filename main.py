# Basic Tic Tac Toe Project. Player vs Computer

board = [' ' for x in range(10)]  # Initialize the board with empty spaces


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):  # Check if the space is free
    return board[pos] == ' '


def printBoard(board):  # Print the board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):  # Check if the player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def playerMove():  # Get player move
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():  # Get computer move
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):  # Select a random item from a list
    import random

    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):  # Check if the board is full
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():  # Main function
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Oops! O has won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('TIE GAME!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move)
                printBoard(board)
        else:
            print('Congratulations! You Won')
            break

    if isBoardFull(board):
        print('TIE GAME!')


main()

# Uncomment the following line to run the program with 'Play Again' option
# while True:
#     input('Press ENTER to start a new game or type \'q\' to quit: ')
#     if input == 'q':
#         break
#     else:
#         board = [' ' for x in range(10)]
#         main()
