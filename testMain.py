import pygame as pg
import sys, task

# Gen Set up
pg.init()

clock = pg.time.Clock()

# Display surface
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800
BLACK = (0, 0, 0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)

#screen_ratio = 0.45
taskWidth = int(DISPLAY_WIDTH * 0.6)
taskHeight = int(DISPLAY_HEIGHT * 0.45)

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
taskSurface = pg.Surface([taskWidth, taskHeight])

# Just for designing
taskSurfaceRect = taskSurface.get_rect(topleft = [(DISPLAY_WIDTH - taskWidth)//2, DISPLAY_HEIGHT//2])
print(taskSurfaceRect.center)

#dragon = pg.image.load('imagefile')

# 
scroll = 0 # vertical displacement

# makes limits (so can't scroll too up or down)

def event_handler(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if self.bar_rect.collidepoint(pos):
                self.mouse_diff = pos[1] - self.bar_rect.y
                self.on_bar = True
            elif self.bar_up.collidepoint(pos):
                self.change_y = 5
            elif self.bar_down.collidepoint(pos):
                self.change_y = -5
                
        if event.type == pg.MOUSEBUTTONUP:
            self.change_y = 0
            self.on_bar = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.change_y = 5
            elif event.key == pg.K_DOWN:
                self.change_y = -5
                
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.change_y = 0
            elif event.key == pg.K_DOWN:
                self.change_y = 0

def menu():
    gameRun = True

    while gameRun:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                gameExit = False
                pg.quit()
                sys.exit()
        gameDisplay.fill((250, 250, 250))
        gameDisplay.blit(taskSurface, taskSurfaceRect)
        #taskSurface.blit(dragon, (x, y))
        
        pg.display.flip() # draws the things on the display so it can be seen
        clock.tick(60)

menu() # Run the main func
