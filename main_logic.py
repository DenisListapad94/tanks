x = "X"
o = "0"
empty = " "
tie = "tie"


def new_board():
    board = []
    for square in range(9):
        board.append(empty)
    return board


def add_sign(board, ind,sign):
    board[ind] = sign
    print(board)
    return board


def legal_moves(board, move):
    if board[move] == empty:
        return True
    else:
        return False


def winner(board):
    win_way = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for row in win_way:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            win = board[row[0]]
            return win
    if empty not in board:
        return tie
    else:
        return None


def computer_choise(board):
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    board1 = board[:]
    for move in range(len(board1)):
        if legal_moves(board1, move):
            board1[move] = '0'
            if winner(board1) == '0':
                return move
            board1[move] = ' '
    board1 = board[:]

    for move in range(len(board)):
        if legal_moves(board1, move):
            board1[move] = 'X'
            if winner(board1) == 'X':
                return move
            board1[move] = ' '

    board1 = board[:]

    for move in BEST_MOVES:
        if legal_moves(board1,move):
            # print(type(move))
            print(move)
            return move

