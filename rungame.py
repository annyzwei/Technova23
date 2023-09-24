import pygame as pg
from button import Button
from datetime import datetime, timedelta
from manipulate_health_data import wrkout_collection
import time
import sys
import random


pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1000
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_BLUE = (202, 239, 250)
WHITE = (255, 255, 255)


DRAGON_ANIMATION_HEIGHT = 300

# Tree parameters
tree_width = 30
tree_height = 60
tree_speed = 5
TREE_GREEN = (34, 139, 34)

# clouds
cloud_width = 130
cloud_height = 40
cloud_speed = 2


dragon_sprite = pg.image.load("assets/dragon.png")

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A Dragon's Guide to Power")
clock = pg.time.Clock()

goals = []
gameRun = True
newGoalRun = True


trees = []
clouds = []

for _ in range(8):  
    x = random.randint(DISPLAY_WIDTH, DISPLAY_WIDTH * 2)
    y = DRAGON_ANIMATION_HEIGHT
    trees.append((x, y))

for _ in range(5):  #
    x = random.randint(DISPLAY_WIDTH, DISPLAY_WIDTH * 2)
    h_variation = random.randint(-15, 15)

    y = 50 + h_variation #height of clouds
    clouds.append((x, y))


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


# Function to draw a triangle tree
def draw_tree(x, y):
    w_variation = 0#random.randint(-5, 5)
    h_variation = 0#random.randint(-5, 10)
    pg.draw.polygon(gameDisplay, TREE_GREEN, [(x, y), (x + (tree_width + w_variation)/ 2, y - (tree_height + h_variation)), (x + tree_width + w_variation, y)])


# Function to draw a cloud
def draw_cloud(x, y):
    pg.draw.ellipse(gameDisplay, WHITE, (x, y, cloud_width, cloud_height))

def dragonAnimation():
    pg.draw.rect(gameDisplay, LIGHT_BLUE, [0, 0, DISPLAY_WIDTH, DRAGON_ANIMATION_HEIGHT])
    dragon_sprite_small = pg.transform.scale(dragon_sprite, (170, 100))
    gameDisplay.blit(dragon_sprite_small, (300, 100))

    clock = pg.time.Clock()

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

        for i in range(len(trees)):
            x, y = trees[i]
            draw_tree(x, y)
            x -= tree_speed
            trees[i] = (x, y)

            # Reset tree's position when it goes off the screen
            if x + tree_width < 0:
                x = DISPLAY_HEIGHT + random.randint(50, 200)
                trees[i] = (x, y)

        for i in range(len(clouds)):
            x, y = clouds[i]
            draw_cloud(x, y)
            x -= cloud_speed
            clouds[i] = (x, y)

            # Reset tree's position when it goes off the screen
            if x + cloud_width < 0:
                x = DISPLAY_HEIGHT + random.randint(50, 200)
                clouds[i] = (x, y) 
        pg.display.flip()


        dragonAnimation()





        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if SKILLS.checkForInput(PLAY_MOUSE_POS):
                    skillsPage()
                elif GOALS.checkForInput(PLAY_MOUSE_POS):
                    newGoalPage()
        pg.display.update()
        #clock.tick(60)

menu()
