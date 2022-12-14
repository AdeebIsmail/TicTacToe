
import turtle as turtle
import numpy as np



def check_up(game_board, count, start, c, player):
    """Checks the whole column for 4 in a row. Will return False if the function reaches the end of the column. Will
    return True if the function detects 3 more corresponding pieces """
    if start == 6:
        return False
    if count == 3:
        return True
    if game_board[start][c] == player:
        try:
            if game_board[start + 1][c] == player:
                count += 1
            else:
                count = 0
        except IndexError:
            return False
    return check_up(game_board, count, start + 1, c, player)


def check_side(game_board, count, start, r, player):
    """Checks the whole row for 4 in a row. Will return False if the function reaches the end of the row. Will return
    True if the function detects 3 more corresponding pieces """
    if start == 7:
        return False
    if count == 3:
        return True
    if game_board[r][start] == player:
        try:
            if game_board[r][start + 1] == player:
                count += 1
            else:
                count = 0
        except IndexError:
            return check_side(game_board, count, start + 1, r, player)
    return check_side(game_board, count, start + 1, r, player)


def check_diagonal_down(game_board, count, r, c, player):
    """Checks how many pieces are downward diagonally going from left to right. It will return how many pieces are
    downward diagonally including itself """
    try:
        if game_board[r][c] == player:
            count += 1
        else:
            return count
    except IndexError:
        return count
    return check_diagonal_down(game_board, count, r + 1, c + 1, player)


def check_diagonal_up(game_board, count, r, c, player):
    try:
        if game_board[r][c] == player:
            count += 1
        else:
            return count
    except IndexError:
        return count
    return check_diagonal_up(game_board, count, r - 1, c - 1, player)


def check_other_diagonal_down(game_board, count, r, c, player):
    try:
        if game_board[r][c] == player:
            count += 1
        else:
            return count
    except IndexError:
        return count
    return check_other_diagonal_down(game_board, count, r + 1, c - 1, player)


def check_other_diagonal_up(game_board, count, r, c, player):
    try:
        if game_board[r][c] == player:
            count += 1
        else:
            return count
    except IndexError:
        return count
    return check_other_diagonal_up(game_board, count, r - 1, c + 1, player)


def valid_input(r, c):
    try:
        if board[r][c] == 0.0 and r != 5 and board[r + 1][c] != 0.0:
            return True
        elif board[r][c] == 0.0 and r == 5:
            return True
        return False
    except IndexError:
        return False


board = np.zeros(shape=(6, 7))

while True:
    row = int(input('Player 1: Enter the Row Coordinate: '))
    col = int(input('Player 1: Enter the Col Coordinate: '))
    while not valid_input(row, col):
        print('\nTry Again\n')
        row = int(input('Player 1: Enter the Row Coordinate: '))
        col = int(input('Player 1: Enter the Col Coordinate: '))
    board[row][col] = 1.0
    print('------------------------')
    print(board)
    print('------------------------')
    if check_up(board, 0, 0, col, 1.0):
        print('\nPlayer 1 wins\n')
        break
    if check_side(board, 0, 0, row, 1.0):
        print('\nPlayer 1 wins\n')
        break
    if check_diagonal_down(board, 0, row, col, 1.0) + check_diagonal_up(board, 0, row, col, 1.0) == 5:
        print('\nPlayer 1 wins\n')
        break
    if check_other_diagonal_down(board, 0, row, col, 1.0) + check_other_diagonal_up(board, 0, row, col, 1.0) == 5:
        print('\nPlayer 1 wins\n')
        break
    row = int(input('Player 2: Enter the Row Coordinate: '))
    col = int(input('Player 2: Enter the Col Coordinate: '))
    while not valid_input(row, col):
        print('\nTry Again\n')
        row = int(input('Player 2: Enter the Row Coordinate: '))
        col = int(input('Player 2: Enter the Col Coordinate: '))
    board[row][col] = 2.0
    print('------------------------')
    print(board)
    print('------------------------')
    if check_up(board, 0, 0, col, 2.0):
        print('\nPlayer 2 wins\n')
        break
    if check_side(board, 0, 0, row, 2.0):
        print('\nPlayer 2 wins\n')
        break
    if check_diagonal_down(board, 0, row, col, 2.0) + check_diagonal_up(board, 0, row, col, 2.0) == 5:
        print('\nPlayer 2 wins\n')
        break
    if check_other_diagonal_down(board, 0, row, col, 2.0) + check_other_diagonal_up(board, 0, row, col, 2.0) == 5:
        print('\nPlayer 2 wins\n')
        break
