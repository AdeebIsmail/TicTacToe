# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Adeeb Ismail
#               NAME OF TEAM MEMBER 2
#               NAME OF TEAM MEMBER 3
#               NAME OF TEAM MEMBER 4
# Section:      554
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

import turtle as turtle
import numpy as np

s = turtle.getscreen()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()


def drawBoard():
    turtle.goto(-30, 385)
    turtle.write("TicTacToe", font=("Verdana", 11, "normal"))
    turtle.goto(-400, -350)
    turtle.pendown()
    turtle.forward(800)

    turtle.left(90)
    turtle.forward(700)

    turtle.left(90)
    turtle.forward(800)

    turtle.left(90)
    turtle.forward(700)
    # draws the columns
    for i in range(6):
        x, y = turtle.pos()
        turtle.goto(x + (800 / 7), y)

        turtle.left(180)
        turtle.forward(700)

    turtle.penup()
    turtle.goto(-400, -350 + 700)
    turtle.pendown()

    x, y = turtle.pos()
    turtle.goto(x, y - (700 / 6))
    turtle.left(90)
    turtle.forward(800)
    # draws the rows
    for i in range(5):
        x, y = turtle.pos()
        turtle.goto(x, y - (700 / 6))
        turtle.left(180)
        turtle.forward(800)

    turtle.penup()
    x, y = turtle.pos()
    turtle.goto(x - 50, y + (800 / 7) / 2)
    turtle.write('5', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x, y + (800 / 7))
    turtle.write('4', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x, y + (800 / 7))
    turtle.write('3', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x, y + (800 / 7))
    turtle.write('2', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x, y + (800 / 7))
    turtle.write('1', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x, y + (800 / 7))
    turtle.write('0', font=("Verdana", 10, "normal"))

    turtle.goto(-400, 350)

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6) / 2, y + 20)
    turtle.write('0', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('1', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('2', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('3', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('4', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('5', font=("Verdana", 10, "normal"))

    x, y = turtle.pos()
    turtle.goto(x + (700 / 6), y)
    turtle.write('6', font=("Verdana", 10, "normal"))


def drawCircle(color, r, c):
    x = -400
    y = -350
    if color == 'red':
        turtle.pencolor('red')
    else:
        turtle.pencolor('black')
    turtle.penup()
    turtle.goto(x + ((c + 1) * (800 / 7)) - ((800 / 7) / 2), y + (6 - r) * (700 / 6) - 10)
    turtle.pendown()
    turtle.circle(50)


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


drawBoard()
board = np.zeros(shape=(6, 7))

while True:
    row = int(input('Player 1: Enter the Row Coordinate: '))
    col = int(input('Player 1: Enter the Col Coordinate: '))
    while not valid_input(row, col):
        print('\nTry Again\n')
        row = int(input('Player 1: Enter the Row Coordinate: '))
        col = int(input('Player 1: Enter the Col Coordinate: '))
    board[row][col] = 1.0
    drawCircle('red', row, col)
    # print('------------------------')
    # print(board)
    # print('------------------------')
    if check_up(board, 0, 0, col, 1.0):
        print('\nPlayer 1 wins\n')
        turtle.done()
        break
    if check_side(board, 0, 0, row, 1.0):
        print('\nPlayer 1 wins\n')
        turtle.done()
        break
    if check_diagonal_down(board, 0, row, col, 1.0) + check_diagonal_up(board, 0, row, col, 1.0) == 5:
        print('\nPlayer 1 wins\n')
        break
    if check_other_diagonal_down(board, 0, row, col, 1.0) + check_other_diagonal_up(board, 0, row, col, 1.0) == 5:
        print('\nPlayer 1 wins\n')
        turtle.done()
        break
    row = int(input('Player 2: Enter the Row Coordinate: '))
    col = int(input('Player 2: Enter the Col Coordinate: '))
    while not valid_input(row, col):
        print('\nTry Again\n')
        row = int(input('Player 2: Enter the Row Coordinate: '))
        col = int(input('Player 2: Enter the Col Coordinate: '))
    board[row][col] = 2.0
    drawCircle('black', row, col)
    # print('------------------------')
    # print(board)
    # print('------------------------')
    if check_up(board, 0, 0, col, 2.0):
        print('\nPlayer 2 wins\n')
        turtle.done()
        break
    if check_side(board, 0, 0, row, 2.0):
        print('\nPlayer 2 wins\n')
        turtle.done()
        break
    if check_diagonal_down(board, 0, row, col, 2.0) + check_diagonal_up(board, 0, row, col, 2.0) == 5:
        print('\nPlayer 2 wins\n')
        turtle.done()
        break
    if check_other_diagonal_down(board, 0, row, col, 2.0) + check_other_diagonal_up(board, 0, row, col, 2.0) == 5:
        print('\nPlayer 2 wins\n')
        turtle.done()
        break

