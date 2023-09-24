# Imports
import pygame as pg
from attributes import appConsts


# scroll bar: from https://github.com/edward344/scrollbar/blob/master/scrollbar.py

screen_width = appConsts.DISPLAY_WIDTH * 0.74
screen_height = appConsts.DISPLAY_HEIGHT * 0.29

GRAY = (197,194,197)
BLUE =(0,0,255)
WHITE = (255,255,255)

class TaskPanel(object):
    
    def __init__(self,image_height):
        self.y_axis = 0
        self.image_height = image_height
        self.change_y = 0
        
        bar_height = int((screen_height - 40) / (image_height / (screen_height * 1.0)))
        self.bar_rect = pg.Rect(screen_width - 20,20,20,bar_height)
        self.bar_up = pg.Rect(screen_width - 20,0,20,20)
        self.bar_down = pg.Rect(screen_width - 20,screen_height - 20,20,20)
        
        self.bar_up_image = pg.image.load("assets/up.png").convert()
        self.bar_down_image = pg.image.load("assets/down.png").convert()
        
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
            print("MOUSEDD BW")
            pos = pg.mouse.get_pos()
            if self.bar_rect.collidepoint(pos):
                self.mouse_diff = pos[1] - self.bar_rect.y
                self.on_bar = True
            elif self.bar_up.collidepoint(pos):
                self.change_y = 10
            elif self.bar_down.collidepoint(pos):
                self.change_y = -10
                
        if event.type == pg.MOUSEBUTTONUP:
            print("MOUSEDD BU")
            self.change_y = 0
            self.on_bar = False
        
        if event.type == pg.KEYDOWN:
            print("MOUSEDD KD")
            if event.key == pg.K_UP:
                self.change_y = 10
            elif event.key == pg.K_DOWN:
                self.change_y = -10
                
        if event.type == pg.KEYUP:
            print("MOUSEDD KU")
            if event.key == pg.K_UP:
                self.change_y = 0
            elif event.key == pg.K_DOWN:
                self.change_y = 0
                
    def draw(self,screen):
        pg.draw.rect(screen,GRAY,self.bar_rect)
        
        screen.blit(self.bar_up_image,(screen_width - 20,0))
        screen.blit(self.bar_down_image,(screen_width - 20,screen_height - 20))

    