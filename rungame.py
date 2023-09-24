import pygame as pg
from button import Button
from datetime import datetime, timedelta
from manipulate_health_data import wrkout_collection
import time
import sys

pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1000
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_BLUE = (202, 239, 250)
WHITE = (255, 255, 255)

DRAGON_ANIMATION_HEIGHT = 300


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
    gameDisplay.fill(WHITE)
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
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
    gameDisplay.fill(WHITE)
    # a: activity type
    # d: distance
    # c: time frame
    active_a = False
    active_d = False
    active_t = False
    activity_text = ""
    distance_text = ""
    time_text = ""
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        largeText = pg.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("Activity: ", largeText, BRIGHT_GREEN)   
        textRect.midright = (300, 450)
        textSurf_dist, textRect_dist = textObjects("Distance: ", largeText, BRIGHT_GREEN)   
        textRect_dist.midright = (300, 500)
        textSurf_time, textRect_time = textObjects("Number of Days: ", largeText, BRIGHT_GREEN)   
        textRect_time.midright = (300, 550)
        gameDisplay.blit(textSurf, textRect)
        gameDisplay.blit(textSurf_dist, textRect_dist)
        gameDisplay.blit(textSurf_time, textRect_time)
       # button("Menu", 50, 400, 100, 75, 20, GREEN, BRIGHT_GREEN, menu )
        pg.display.update()
        MAINMENU = Button(image=None, pos=(640, 460), 
                            text_input="MAIN MENU", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        MAINMENU.changeColor(PLAY_MOUSE_POS)
        MAINMENU.update(gameDisplay)

        text_surface_a = largeText.render(activity_text, True, BLACK)
        input_rect_a = pg.Rect(350, 430, 300, 40)

        text_surface_d = largeText.render(distance_text, True, BLACK)
        input_rect_d = pg.Rect(350, 480, 300, 40)

        text_surface_t = largeText.render(time_text, True, BLACK)
        input_rect_t = pg.Rect(350, 530, 300, 40)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if MAINMENU.checkForInput(PLAY_MOUSE_POS):
                    menu()
                active_a = False
                active_d = False
                active_t = False
                if input_rect_a.collidepoint(event.pos):
                    active_a = True
                elif input_rect_d.collidepoint(event.pos):
                    active_d = True
                elif input_rect_t.collidepoint(event.pos):
                    active_t = True
                # text_surface = largeText.render(input_text, True, BLACK)
            elif event.type == pg.KEYDOWN:
                gameDisplay.fill(WHITE)
                pg.display.update([input_rect_a, input_rect_d, input_rect_t])
                if active_a:
                    if event.key == pg.K_RETURN:
                        print("User Input:", activity_text)
                        activity_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        activity_text = activity_text[:-1]
                    else:
                        activity_text += event.unicode
                    text_surface_a = largeText.render(activity_text, True, BLACK)
                if active_d:
                    if event.key == pg.K_RETURN:
                        print("User Input:", distance_text)
                        distance_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        distance_text = distance_text[:-1]
                    else:
                        distance_text += event.unicode
                    text_surface = largeText.render(distance_text, True, BLACK)
                if active_t:
                    if event.key == pg.K_RETURN:
                        print("User Input:", time_text)
                        time_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        time_text = time_text[:-1]
                    else:
                        time_text += event.unicode
                    text_surface = largeText.render(time_text, True, BLACK)
        pg.draw.rect(gameDisplay, BLACK, input_rect_a, 2)
        gameDisplay.blit(text_surface_a, (input_rect_a.x + 5, input_rect_a.y + 5))
        pg.draw.rect(gameDisplay, BLACK, input_rect_d, 2)
        gameDisplay.blit(text_surface_d, (input_rect_d.x + 5, input_rect_d.y + 5))
        pg.draw.rect(gameDisplay, BLACK, input_rect_t, 2)
        gameDisplay.blit(text_surface_t, (input_rect_t.x + 5, input_rect_t.y + 5))
        pg.display.update([input_rect_a, input_rect_d, input_rect_t])
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
