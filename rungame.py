import pygame as pg
from button import Button
from datetime import datetime, timedelta
from manipulate_health_data import wrkout_collection
import taskPanel, scrollTest
from attributes import appConsts
import sys

pg.init()

DISPLAY_WIDTH = appConsts.DISPLAY_WIDTH
DISPLAY_HEIGHT = appConsts.DISPLAY_HEIGHT
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_BLUE = (202, 239, 250)
WHITE = (255, 255, 255)

DRAGON_ANIMATION_HEIGHT = 300


taskWidth = int(DISPLAY_WIDTH * 0.75)
taskHeight = int(DISPLAY_HEIGHT * 0.3)

taskSurface = pg.Surface([taskWidth, taskHeight])
taskSurface.fill(LIGHT_BLUE)


dragon_sprite = pg.image.load("assets/dragon.png")

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A Dragon's Guide to Power")
clock = pg.time.Clock()

goals = []
gameRun = True
newGoalRun = True

def textObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    #returns text + rectangle
    return textSurface, textSurface.get_rect()


def skillsPage():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        gameDisplay.fill(WHITE)
        largeText = pg.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("HIGHSCORE: ", largeText, BRIGHT_GREEN)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)
        pg.display.update()
        MAINMENU = Button(image=None, pos=(640, 460), 
                            text_input="MAIN MENU", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        MAINMENU.changeColor(PLAY_MOUSE_POS)
        MAINMENU.update(gameDisplay)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if MAINMENU.checkForInput(PLAY_MOUSE_POS):
                    menu()
        pg.display.update()
        #clock.tick(60)

def newGoalPage():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        gameDisplay.fill(WHITE)
        largeText = pg.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("Add A New Goal: ", largeText, BRIGHT_GREEN)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)
       # button("Menu", 50, 400, 100, 75, 20, GREEN, BRIGHT_GREEN, menu )
        pg.display.update()
        MAINMENU = Button(image=None, pos=(640, 460), 
                            text_input="MAIN MENU", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        MAINMENU.changeColor(PLAY_MOUSE_POS)
        MAINMENU.update(gameDisplay)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if MAINMENU.checkForInput(PLAY_MOUSE_POS):
                    menu()
        pg.display.update()
        #clock.tick(60)

def dragonAnimation():
    pg.draw.rect(gameDisplay, LIGHT_BLUE, [0, 0, DISPLAY_WIDTH, DRAGON_ANIMATION_HEIGHT])
    dragon_sprite_small = pg.transform.scale(dragon_sprite, (170, 100))
    gameDisplay.blit(dragon_sprite_small, (300, 100))

def dragonAnimation():
    pg.draw.rect(gameDisplay, LIGHT_BLUE, [0, 0, DISPLAY_WIDTH, DRAGON_ANIMATION_HEIGHT])
    dragon_sprite_small = pg.transform.scale(dragon_sprite, (170, 100))
    gameDisplay.blit(dragon_sprite_small, (300, 100))

def menu():
    d = datetime(2023, 9, 1)
    gameRun = True
    start_time = datetime.now()

    while gameRun:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        if (datetime.now() - start_time).total_seconds() > 5:
            start_time = datetime.now()
            d += timedelta(days=1)

        gameDisplay.fill(WHITE)

        dragonAnimation()

        largeText = pg.font.SysFont('garamond', 20)
        textSurf, textRect = textObjects("Date: " + str(d.date()), largeText, BLACK)   
        textRect.center = (400, 200)
        gameDisplay.blit(textSurf, textRect)

        


       # displayProfile()

      #  displayMissions()
        SKILLS = Button(image=None, pos=(200, 460), 
                            text_input="SKILLZ", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        SKILLS.changeColor(PLAY_MOUSE_POS)
        SKILLS.update(gameDisplay)

              #  displayMissions()
        GOALS = Button(image=None, pos=(640, 460), 
                            text_input="GOALS", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        GOALS.changeColor(PLAY_MOUSE_POS)
        GOALS.update(gameDisplay)
        
            
            
        # --- Game logic should go here
        
        # Create scroll bar object
        image = pg.image.load("assets/background.jpeg").convert()
        scrollbar = taskPanel.TaskPanel(image.get_height())
        #taskPanel.TaskPanel(image.get_height()) # Make it so that the image of the height corresponds to the # of tasks

        scrollbar.update()
        
        # --- Drawing code should go here
        taskSurface.blit(image, (0,scrollbar.y_axis))
        scrollbar.draw(taskSurface)
        gameDisplay.blit(taskSurface, [(DISPLAY_WIDTH - taskWidth)//2, DISPLAY_HEIGHT//2])
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if SKILLS.checkForInput(PLAY_MOUSE_POS):
                    skillsPage()
                elif GOALS.checkForInput(PLAY_MOUSE_POS):
                    newGoalPage()
            scrollbar.event_handler(event)
        pg.display.update()
        #clock.tick(60)

menu()
