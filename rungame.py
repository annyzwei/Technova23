import pygame as pg
from button import Button
from datetime import datetime, timedelta
from manipulate_health_data import wrkout_collection
import taskPanel, scrollTest, task
from attributes import appConsts
import sys
import random


pg.init()

DISPLAY_WIDTH = appConsts.DISPLAY_WIDTH
DISPLAY_HEIGHT = appConsts.DISPLAY_HEIGHT
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_BLUE = (202, 239, 250)
WHITE = (255, 255, 255)
BEIGE = (250, 241, 225)


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

# Subsurface for goals
taskWidth = int(DISPLAY_WIDTH * 0.75)
taskHeight = int(DISPLAY_HEIGHT * 0.3)

taskSurface = pg.Surface([taskWidth, taskHeight])
taskSurface.fill(LIGHT_BLUE)

dragon_sprite = pg.image.load("assets/dragon.png")
scroll_sprite = pg.image.load("assets/scroll.png")

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("A Dragon's Guide to Power")
clock = pg.time.Clock()

goals = []
gameRun = True
newGoalRun = True


trees = []
clouds = []

largeText = pg.font.SysFont('garamond', 20)

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
        clock.tick(60)

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
        textSurf_dist, textRect_dist = textObjects("Distance(km): ", largeText, BRIGHT_GREEN)   
        textRect_dist.midright = (300, 500)
        textSurf_time, textRect_time = textObjects("Number of Days to Complete it: ", largeText, BRIGHT_GREEN)   
        textRect_time.midright = (300, 550)
        gameDisplay.blit(textSurf, textRect)
        gameDisplay.blit(textSurf_dist, textRect_dist)
        gameDisplay.blit(textSurf_time, textRect_time)
       # button("Menu", 50, 400, 100, 75, 20, GREEN, BRIGHT_GREEN, menu )
        pg.display.update()
        MAINMENU = Button(image=None, pos=(500, 375), 
                            text_input="MAIN MENU", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        MAINMENU.changeColor(PLAY_MOUSE_POS)
        MAINMENU.update(gameDisplay)
        
        SUBMIT = Button(image=None, pos=(500, 625), 
                            text_input="SUBMIT", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        SUBMIT.changeColor(PLAY_MOUSE_POS)
        SUBMIT.update(gameDisplay)

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
                elif SUBMIT.checkForInput(PLAY_MOUSE_POS):
                    # Create goal and head back to the main menu
                    goals.append(task.Task(activity_text, time_text, distance_text))
                    print(goals[0].activity)
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
                    elif event.unicode.isdigit():
                        distance_text += event.unicode
                    text_surface = largeText.render(distance_text, True, BLACK)
                if active_t:
                    if event.key == pg.K_RETURN:
                        print("User Input:", time_text)
                        time_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        time_text = time_text[:-1]
                    elif event.unicode.isdigit():
                        time_text += event.unicode
                    text_surface = largeText.render(time_text, True, BLACK)
        pg.draw.rect(gameDisplay, BLACK, input_rect_a, 2)
        gameDisplay.blit(text_surface_a, (input_rect_a.x + 5, input_rect_a.y + 5))
        pg.draw.rect(gameDisplay, BLACK, input_rect_d, 2)
        gameDisplay.blit(text_surface_d, (input_rect_d.x + 5, input_rect_d.y + 5))
        pg.draw.rect(gameDisplay, BLACK, input_rect_t, 2)
        gameDisplay.blit(text_surface_t, (input_rect_t.x + 5, input_rect_t.y + 5))
        pg.display.update([input_rect_a, input_rect_d, input_rect_t])
        clock.tick(60)



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
    pg.draw.rect(gameDisplay, TREE_GREEN, [0, DRAGON_ANIMATION_HEIGHT, DISPLAY_WIDTH, 10])
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

        # Reset clouds's position when it goes off the screen
        if x + cloud_width < 0:
            x = DISPLAY_HEIGHT + random.randint(50, 200)
            clouds[i] = (x, y) 

    dragon_sprite_small = pg.transform.scale(dragon_sprite, (190, 100))
    gameDisplay.blit(dragon_sprite_small, (300, 100))


def displayTimeScroll(d):
        scroll_x = 200
        scroll_y = 0 
        scroll_w = 350
        scroll_h = 100

        scroll_sprite_small = pg.transform.scale(scroll_sprite, (scroll_w, scroll_h))
        gameDisplay.blit(scroll_sprite_small, (scroll_x, scroll_y))

        largeText = pg.font.SysFont('garamond', 20)
        textSurf, textRect = textObjects("Date: " + str(d.date()), largeText, BLACK)   
        textRect.center = (scroll_x + scroll_w/2, scroll_y + scroll_h/2)
        gameDisplay.blit(textSurf, textRect)

        

def menu():
    d = datetime(2023, 9, 1)
    gameRun = True
    start_time = datetime.now()
    
    # Create scroll bar object
    image = pg.image.load("assets/background.jpeg").convert()
    # Create scrollbar object 
    scrollbar = taskPanel.TaskPanel(image.get_height())
    rect_objects = []
    for i in range(20):
        rect = pg.Rect(50, 50 + i * 30, DISPLAY_WIDTH * 0.75, 20)
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rect_objects.append((rect, colour))
    text_Objects = []
    for i in range(20):
        largeText = pg.font.SysFont('garamond', 20)
        textSurf, textRect = textObjects("Goal!", largeText, BLACK)  
        textRect.x = 50
        textRect.y = scrollbar.y_axis + i * 30
        textRect.width = DISPLAY_WIDTH * 0.75
        textRect.height = 20 
        text_Objects.append([textSurf, textRect, textRect.y])


    pg.display.flip()

    while gameRun:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        if (datetime.now() - start_time).total_seconds() > 5:
            start_time = datetime.now()
            d += timedelta(days=1)

        gameDisplay.fill(BEIGE)

        largeText = pg.font.SysFont('garamond', 20)

        # displayProfile()

        # displayMissions()

        SKILLS = Button(image=None, pos=(200, 460), 
                            text_input="SKILLZ", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        SKILLS.changeColor(PLAY_MOUSE_POS)
        SKILLS.update(gameDisplay)

              #  displayMissions()
        GOALS = Button(image=None, pos=(640, 460), 
                            text_input="GOALS", font=largeText, base_color=GREEN, hovering_color=BRIGHT_GREEN)

        GOALS.changeColor(PLAY_MOUSE_POS)
        GOALS.update(gameDisplay)
        dragonAnimation()
        displayTimeScroll(d)
        

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
            
       
         # --- Game logic should go here
        scrollbar.update()

        # --- Drawing code should go here
        taskSurface.blit(image,(0,scrollbar.y_axis))
        for text in text_Objects:
            #taskSurface.blit(pg.Surface((rect[0].w, rect[0].h)), (0, scrollbar.y_axis + rect[0].y))
            text[1].y = scrollbar.y_axis + text[2]
            taskSurface.blit(text[0], text[1])
            scrollbar.draw(taskSurface)
        gameDisplay.blit(taskSurface, [(DISPLAY_WIDTH - taskWidth)//2, DISPLAY_HEIGHT * 0.5])
        
        
        pg.display.flip()
        clock.tick(60)


menu()
