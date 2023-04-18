import pygame
from tic_tac_toe_menu import *
from main_logic import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

W, H = 490, 620
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

flmenu = True
flplay = False

lst_cord = [[10, 140, 150, 150],
            [170, 140, 150, 150],
            [330, 140, 150, 150],
            [10, 300, 150, 150],
            [170, 300, 150, 150],
            [330, 300, 150, 150],
            [10, 460, 150, 150],
            [170, 460, 150, 150],
            [330, 460, 150, 150]]

dict_board = {i: lst_cord[i] for i in range(len(lst_cord))}
board = new_board()
flcomp = False


def human_move(flcomp):
    global board
    for lst in lst_cord:
        if lst[0] < event.pos[0] < lst[0] + lst[2] and lst[1] < event.pos[1] < lst[1] + lst[3]:
            list_figure(1, lst[0], lst[1])
            for i in range(len(lst_cord)):
                if lst[0] == lst_cord[i][0] and lst[1] == lst_cord[i][1]:
                    board = add_sign(board, i, "X")
                    flcomp = True
    return flcomp


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not flcomp:
                flcomp = human_move(flcomp)
            if flcomp and winner(board) != 'tie':
                comp_move = computer_choise(board)
                board = add_sign(board, comp_move, "0")
                list_figure(2, lst_cord[comp_move][0], lst_cord[comp_move][1])
                flcomp = False

    Display_board(sc, FPS)

    if winner(board) == "X":
        print("X-win")
        break
    elif winner(board) == "0":
        print("0-win")
        break
    elif winner(board) == "tie":
        print("tie")
        break
