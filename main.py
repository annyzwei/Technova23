#Import game modules
import pygame 
import time
import random
import pygame, sys
pygame.init()

#Declaration of variables
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200,0,0)
GREEN = (0,200,0)
YELLOW = (200, 200, 0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
BRIGHT_YELLOW = (255, 255, 0)

#Import images and sound
logo = pygame.image.load("Logo.png")
pop = pygame.mixer.Sound("pop.wav")
bounce = pygame.mixer.Sound("bounce.wav")
game_over = pygame.mixer.Sound("gameover.wav")
win = pygame.mixer.Sound("win.wav")
ding = pygame.mixer.Sound("ding.wav")
background_music = pygame.mixer.music.load('fizzy.wav')
highscore = [0]
wins = []
losses = []

paused = True


# Setting the dimensions of the game screen
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("A Dragon's Guide to Power")
clock = pygame.time.Clock()



#Changes colour based on length of the paddle
def colour(length):
    target = length//10
    #changes the colour using rgb scale
    red = (10-target)*28.3 
    green = (target-1)*28.3
    colour = (red, green, 0)
    return colour

#Function to display the number of bounces
def successful_bounces(count):  
    font = pygame.font.SysFont(None, 25)
    text = font.render("Bounces: " +str(count), True, WHITE)
    gameDisplay.blit(text, (5, 5))#coordinates of text


#appearance and coordinates of paddle
def paddle(x, width):
    paddle_colour = colour(width)
    pygame.draw.rect(gameDisplay, paddle_colour, [x, 550, width, 15])

#appearance and coordinates of ball
def ball(x, y):
    pygame.draw.circle(gameDisplay, WHITE, [x, y], 10)

#displays game over message
def gameover():
    messageDisplay("GAME OVER", (DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
    
#Sets the surface which the text is on
def textObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    #returns text + rectangle
    return textSurface, textSurface.get_rect()

#Returns font, size and place of text
def messageDisplay(text, x, y):
    #set largetext's font + size
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = textObjects(text, largeText, WHITE)   
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

#Exits the game
def quitGame():
    pygame.quit()
    sys.exit()
    quit()

#Creates a clickable button
def button(text, x, y, width, height, size, icolour, acolour, action = None):
    #Detects user input from mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Checks position of mouse to be in the button area
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolour,(x, y, width, height))
        if click[0] == 1 and action != None:
            action() #activates action
    else:
        #Changes button colour
        pygame.draw.rect(gameDisplay, icolour,(x, y, width, height))

    #Text of button
    largeText = pygame.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjects(text, largeText, BLACK)   
    textRect.center = (x+(width/2), y+(height/2))
    gameDisplay.blit(textSurf, textRect)

#Loads image of powerup
def powerup(x, y):
    power_up = pygame.image.load("powerup.png")
    gameDisplay.blit(power_up, (x, y))

#Returns to game
def resume():
    global paused
    paused = False

#Messages displayed when game is won
def win_game():
    time.sleep(1)
    #############
    pygame.mixer.Sound.play(win)
    #############
    
    while paused:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        gameDisplay.fill(BLACK)
        #Tells user their victory
        messageDisplay("YOU WON!", (DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2)- 50)

        #Buttons as to continue the game or leave it
        button("CONTINUE?", 250, 330, 300, 50, 20, BRIGHT_GREEN, GREEN, resume)
        button("BACK TO MENU", 250, 400, 300, 50, 20, BRIGHT_RED, RED, menu)
        pygame.display.update()
        clock.tick(10)
   
def menu():
    #Declaration of variables    
    gameExit = True
    ball_x = 10
    ball_y = 590
    ball_direction_x = 5
    ball_direction_y = -8
    ############
    pygame.mixer.music.load('fizzy.wav')
    pygame.mixer.music.play(-1)
    ############

    while gameExit:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = False
                quit()
        gameDisplay.fill(BLACK)

        #Bounces ball off sides of screen
        if ball_y > DISPLAY_HEIGHT-10 or ball_y <= 10:
            ball_direction_y *= -1
        if ball_x < 10 or ball_x > DISPLAY_WIDTH-10:
            ball_direction_x *= -1

        #background ball coordinates
        ball(ball_x, ball_y)
        ball_x += ball_direction_x
        ball_y += ball_direction_y

        #Loads image of "PONG!"
        gameDisplay.blit(logo, (210, 100))

        #Displays highscore
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("HIGHSCORE: "+str(highscore[-1]), largeText, BRIGHT_YELLOW)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)

        #Displays number of wins
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("WINS: "+str(wins. count('1')), largeText, BRIGHT_GREEN)   
        textRect.center = (200, 300)
        gameDisplay.blit(textSurf, textRect)

        #Displays number of losses
        largeText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("LOSSES: "+str(losses. count('1')), largeText, BRIGHT_RED)   
        textRect.center = (600, 300)
        gameDisplay.blit(textSurf, textRect)

        #Buttons to quit, start, and how to play the game
        button("QUIT", 500, 350, 200, 50, 20, BRIGHT_RED, RED, quitGame)      
        button("START", 100, 350, 200, 50, 20, BRIGHT_GREEN, GREEN, gameLoop)
        button("HOW TO PLAY", 300, 350, 200, 50, 20, BRIGHT_YELLOW, YELLOW, instructions)
 
        pygame.display.update()
        clock.tick(60)

#Displays game instructions
def instructions():
    gameExit = True

    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = False
                quit()
            
        gameDisplay.fill(BLACK)

        #Loads image of instructions because I was lazy to code it
        instructions = pygame.image.load("instructions.png")
        gameDisplay.blit(instructions, (20, 10))
        #Button to start the game
        button("GOT IT, LET'S PLAY!", 450, 450, 300, 50, 20, BRIGHT_GREEN, GREEN, gameLoop)

        pygame.display.update()
        clock.tick(40)

def 

#Code to run the actual game
def gameLoop():

    global paused
    ############
    pygame.mixer.music.fadeout(1)
    #############

    #original starting positions of padde, ball, and powerup
    rect_x = (DISPLAY_WIDTH * 0.45)
    rect_width = 100
    xVelocity = 0
    check = random.randint(1,2)
    if check == 1:
        ball_direction_x = -4
    else:
        ball_direction_x = 4
    ball_direction_y = -6
    ball_x = (random.randint(10, rect_x-10) or random.randint(rect_x+rect_width+10, DISPLAY_WIDTH-10))
    ball_y = 580
    bounces = 0
    count = 0
    powerup_x = random.randint(100, 440)
    powerup_y = random.randint(200, 340)
    
    gameExit = False

    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Controls for the paddle
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    xVelocity = -8
                elif event.key == pygame.K_RIGHT:
                    xVelocity = 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xVelocity = 0
        if rect_x + xVelocity < DISPLAY_WIDTH - (rect_width-5) and rect_x + xVelocity > -5:
            rect_x += xVelocity #adds user input to paddle coordinates

        gameDisplay.fill(BLACK)
        
        #options to quit the game and return to menu
        button("BACK TO MENU", 710, 5, 90, 30, 10, BRIGHT_YELLOW, YELLOW, menu)
        button("QUIT", 710, 40, 90, 30, 10, BRIGHT_RED, RED, quitGame)
        
        #use coordinates to relocate the objects on screen
        paddle(rect_x, rect_width)
        powerup(powerup_x, powerup_y)
        ball(ball_x, ball_y)

        ball_x += ball_direction_x
        ball_y += ball_direction_y

        #Ends game if ball touches the bottom of screen
        if ball_y >= DISPLAY_HEIGHT-10:
            #############
            pygame.mixer.Sound.play(game_over)
            #############
            time.sleep(1)
            font = pygame.font.SysFont(None, 40)
            #Displays final score
            text = font.render("Your final score is: " +str(bounces), True, WHITE)
            gameDisplay.blit(text, (280, 350))
            highscore.append(bounces)
            highscore.sort()

            #Checks to see if latest score is a highscore
            if bounces == highscore[-1]:
                font = pygame.font.SysFont(None, 20)
                text = font.render("NEW HIGHSCORE!", True, BRIGHT_YELLOW)
                gameDisplay.blit(text, (350, 400))
            #Wins and losses count
            if bounces >= 10:
                wins.append("1")
            else:
                losses.append("1")
                
            gameover()
            time.sleep(3)
            gameExit = True
            
        #Bounces ball if it touches the sides 
        if ball_x <= 10 or ball_x >= DISPLAY_WIDTH-10:
            #############
            pygame.mixer.Sound.play(pop)
            #############
            ball_direction_x = -1*ball_direction_x
        if ball_y <= 10:
            #############
            pygame.mixer.Sound.play(pop)
            #############
            ball_direction_y = -1*ball_direction_y

        #Bounces ball if it touches paddle top surface
        if ball_x >= rect_x and ball_x <= rect_x+rect_width:
            if ball_y >= DISPLAY_HEIGHT-60 and ball_y <= DISPLAY_HEIGHT - 35:
                #############
                pygame.mixer.Sound.play(bounce)
                #############
                ball_direction_y = -1*ball_direction_y
                if rect_width > 10:
                    #Decreases paddle width
                    rect_width += -10
                bounces += 1
                
        #Bounces ball if it touches side of paddle
        elif ball_y >= DISPLAY_HEIGHT-60:
            if (ball_x >= rect_x-10 and ball_x <= rect_x+10) or (ball_x >= rect_x+rect_width-10 and ball_x <= rect_x+rect_width+10):
                #############
                pygame.mixer.Sound.play(bounce)
                #############
                ball_direction_x = -1*ball_direction_x

        #Checks if ball is within range of powerup
        if ball_x >= powerup_x and ball_x <= powerup_x +60:
            if ball_y >= powerup_y and ball_y <= powerup_y+60:
                if rect_width < 100:
                    #Adds to paddle width
                    rect_width += 10
                powerup_x = random.randint(100, 440)
                powerup_y = random.randint(200, 340)
                #############
                pygame.mixer.Sound.play(ding)
                #############

        #Displays the number of paddle bounces
        successful_bounces(bounces)

        #Initiates win function when ball is bounced 10 tiems
        if bounces == 10 and count != 1:
            win_game()
            count = 1
            
        #refreshes page
        pygame.display.update()
        clock.tick(60)
    #returns to menu
    menu()

#Main program
menu()