import pygame as pg
from datetime import datetime, timedelta
from manipulate_health_data import wrkout_collection
from pgu import gui

pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1000
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
WHITE = (255, 255, 255)

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A Dragon's Guide to Power")

goals = []
gameRun = True


def textObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    #returns text + rectangle
    return textSurface, textSurface.get_rect()

#size -> fontsize
def button(text, x, y, width, height, size, icolour, acolour, action = None):
    #Detects user input from mouse
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    #Checks position of mouse to be in the button area
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pg.draw.rect(gameDisplay, acolour,(x, y, width, height))
        if click[0] == 1 and action != None:
            action() #activates action
    else:
        #Changes button colour
        pg.draw.rect(gameDisplay, icolour,(x, y, width, height))

    #Text of button
    largeText = pg.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjects(text, largeText, BLACK)   
    textRect.center = (x+(width/2), y+(height/2))
    gameDisplay.blit(textSurf, textRect)

def skillsPage():
    while True:
        gameRun = False
        largeText = pg.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("HIGHSCORE: ", largeText, BRIGHT_GREEN)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)
        pg.display.update()

def menu():
    d = datetime(2023, 9, 1)

    start_time = datetime.now()
    while gameRun:
        if (datetime.now() - start_time).total_seconds() > 5:
            start_time = datetime.now()
            d += timedelta(days=1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                gameExit = False
                quit()
        gameDisplay.fill(WHITE)

        largeText = pg.font.SysFont('garamond', 20)
        textSurf, textRect = textObjects("Date: " + str(d.date()), largeText, BLACK)   
        textRect.center = (400, 200)
        gameDisplay.blit(textSurf, textRect)


       # displayDragonAnimation()

       # displayProfile()

      #  displayMissions()

        button("Skills", 50, 400, 100, 75, 20, GREEN, BRIGHT_GREEN, skillsPage )
        button("+ Goal", 50, 500, 100, 75, 20, GREEN, BRIGHT_GREEN)

        pg.display.update()

menu()
