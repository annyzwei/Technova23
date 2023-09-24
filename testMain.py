## DON'T MIND THISSS~ TESTING

import pygame as pg
import sys, taskPanel

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
gameDisplay.fill((250, 250, 250))
taskSurface = pg.Surface([taskWidth, taskHeight])

# Just for designing
taskSurfaceRect = taskSurface.get_rect(topleft = [(DISPLAY_WIDTH - taskWidth)//2, DISPLAY_HEIGHT//2])
print(taskSurfaceRect.center)

#dragon = pg.image.load('imagefile')

# 
#scroll = 0 # vertical displacement

# makes limits (so can't scroll too up or down)
"""
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
                self.change_y = 0"""

def main():
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()
    # Load Image:
    image = pg.image.load("assets/background.jpeg").convert()
    # Create scrollbar object 
    scrollbar = taskPanel.TaskPanel(image.get_height())
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pg.event.get(): # User did something
            if event.type == pg.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            
            scrollbar.event_handler(event)
            
        # --- Game logic should go here
        scrollbar.update()
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        taskSurface.fill((255,255,255))

        # --- Drawing code should go here
        taskSurface.blit(image,(0,scrollbar.y_axis))
        scrollbar.draw(taskSurface)
        gameDisplay.blit(taskSurface, [(DISPLAY_WIDTH - taskWidth)//2, DISPLAY_HEIGHT//2])
        # --- Update the screen with what was drawn
        pg.display.flip()

        # --- Limit to 30 frames per second
        clock.tick(30)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pg.quit()

# Runs the main func
if __name__ == '__main__':
    main()