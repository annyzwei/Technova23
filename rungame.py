import pygame as pg

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1200
BLACK = (0, 0, 0)

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A Dragon's Guide to Power")


def menu():
    gameRun = True

    while gameRun:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                pg.quit()
                gameExit = False
                quit()
        gameDisplay.fill(BLACK)
        pg.display.update()


menu()
