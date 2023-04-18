import pygame

pygame.init()

d_figure = {}


def Drawmenu(screen, FPS):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    f1 = pygame.font.SysFont('arial', 30)
    text1 = f1.render("START", False, WHITE)
    f2 = pygame.font.SysFont('arial', 30)
    text2 = f1.render("CONTINUE", False, WHITE)
    f3 = pygame.font.SysFont('arial', 30)
    text3 = f1.render("PLAY WITH COMPUTER", False, WHITE)
    f4 = pygame.font.SysFont('arial', 30)
    text4 = f1.render("PLAY WITH PEOPLE", False, WHITE)
    f5 = pygame.font.SysFont('arial', 30)
    text5 = f1.render("EXIT", False, WHITE)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [45, 60, 400, 80])
        pygame.draw.rect(screen, BLACK, [45, 160, 400, 80])
        pygame.draw.rect(screen, BLACK, [45, 260, 400, 80])
        pygame.draw.rect(screen, BLACK, [45, 360, 400, 80])
        pygame.draw.rect(screen, BLACK, [45, 460, 400, 80])

        screen.blit(text1, (180, 80))
        screen.blit(text2, (150, 180))
        screen.blit(text3, (65, 280))
        screen.blit(text4, (160, 380))
        screen.blit(text5, (200, 480))

        pygame.display.update()
        clock.tick(FPS)
        return screen


def Display_board(screen, FPS):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    clock = pygame.time.Clock()

    f1 = pygame.font.SysFont('arial', 30)
    text1 = f1.render("TIC TAK TOE GAME", False, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(WHITE)

        pygame.draw.rect(screen, BLACK, [10, 30, 470, 80])
        screen.blit(text1, (80, 50))

        pygame.draw.rect(screen, BLACK, [10, 140, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [10, 300, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [10, 460, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [170, 140, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [170, 300, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [170, 460, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [330, 140, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [330, 300, 150, 150], 5)
        pygame.draw.rect(screen, BLACK, [330, 460, 150, 150], 5)

        if d_figure != {}:
            for key, value in d_figure.items():
                figure(screen, FPS, value, key[0], key[1])

        pygame.display.update()
        clock.tick(FPS)
        return screen


def list_figure(sign, *args):
    d_figure[args] = sign


def figure(screen, FPS, sign, X1, Y1):

    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    if sign == 1:
        pygame.draw.rect(screen, GREEN, [X1, Y1, 150, 150])
        pygame.draw.line(screen, BLACK, (X1 + 5, Y1 + 5), (X1 + 150 - 5, Y1 + 150 - 5), 10)
        pygame.draw.line(screen, BLACK, (X1 + 150 - 5, Y1 + 5), (X1 + 5, Y1 + 150 - 5), 10)
        return screen
    elif sign == 2:
        pygame.draw.rect(screen, RED, [X1, Y1, 150, 150])
        pygame.draw.circle(screen, BLACK, ((X1 + 75), (Y1 + 75)), 70, 10)
        return screen