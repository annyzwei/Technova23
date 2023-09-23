# Imports
import pygame as pg
import rungame


class ScrollBar(object):
    def __init__(self,image_height):
        self.y_axis = 0
        self.image_height = image_height
        self.change_y = 0
            
        bar_height = int((screen_height - 40) / (image_height / (screen_height * 1.0)))
        self.bar_rect = pygame.Rect(screen_width - 20,20,20,bar_height)
        self.bar_up = pg.Rect(screen_width - 20,0,20,20)
        self.bar_down = pg.Rect(screen_width - 20,screen_height - 20,20,20)
        
        self.bar_up_image = pg.image.load("up.png").convert()
        self.bar_down_image = pg.image.load("down.png").convert()
        
        self.on_bar = False
        self.mouse_diff = 0
        
    def update(self):
        self.y_axis += self.change_y
        
        if self.y_axis > 0:
            self.y_axis = 0
        elif (self.y_axis + self.image_height) < screen_height:
            self.y_axis = screen_height - self.image_height
            
        height_diff = self.image_height - screen_height
        
        scroll_length = screen_height - self.bar_rect.height - 40
        bar_half_lenght = self.bar_rect.height / 2 + 20
        
        if self.on_bar:
            pos = pg.mouse.get_pos()
            self.bar_rect.y = pos[1] - self.mouse_diff
            if self.bar_rect.top < 20:
                self.bar_rect.top = 20
            elif self.bar_rect.bottom > (screen_height - 20):
                self.bar_rect.bottom = screen_height - 20
            
            self.y_axis = int(height_diff / (scroll_length * 1.0) * (self.bar_rect.centery - bar_half_lenght) * -1)
        else:
            self.bar_rect.centery =  scroll_length / (height_diff * 1.0) * (self.y_axis * -1) + bar_half_lenght
            
        
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
                
    def draw(self,screen):
        pg.draw.rect(screen,GRAY,self.bar_rect)
        
        screen.blit(self.bar_up_image,(screen_width - 20,0))
        screen.blit(self.bar_down_image,(screen_width - 20,screen_height - 20))
   
   

class taskPanel():

    # Initialise panel/surface
    screen_ratio = 0.4
    background = pg.Surface(screen.get_size() * screen_ratio)  # where screen is the size of the main screen from rungame
    background = background.convert()           # converts to a single pixel format (speed up run time)
    background.fill((250, 250, 250))            # background colour: white 
    
    screen_width = screen.get_width() * screen_ratio
    screen_height = screen.get_height() * screen_ratio
    
    
    # need to blit objects!! (like show/refresh/place)
    
    # scroll bar: from https://github.com/edward344/scrollbar/blob/master/scrollbar.py

    GRAY = (197,194,197)
    BLUE = (0,0,255)
    WHITE = (255,255,255)
    
     # Used to manage how fast the screen updates
    #clock = pg.time.Clock()
    
    # Load Image:
    image = pg.image.load("instruments.png").convert()
    # Create scrollbar object 
    scrollbar = ScrollBar(image.get_height())
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
        screen.fill((255,255,255))

        # --- Drawing code should go here
        screen.blit(image,(0,scrollbar.y_axis))
        scrollbar.draw(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pg.display.flip()

        # --- Limit to 30 frames per second
        clock.tick(30)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pg.quit()         
        

#def main():
    # Initialize all imported pg.modules
    #pg.init()
    # Set the width and height of the screen [width, height]
    #screen = pg.display.set_mode((screen_width,screen_height))
    # Set the current window caption
    #pg.display.set_caption("ScrollBar")
    #Loop until the user clicks the close button.
    #done = False
   


