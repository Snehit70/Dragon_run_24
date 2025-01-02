import pygame
from pygame.sprite import Sprite
from screen_settings import Settings

class Dragon(Sprite):
    """A class for dragon and its functions."""
    
    def __init__(self):
        """Initializing dragon class."""
        super().__init__()
        
        self.settings = Settings()
        
        self.image = pygame.image.load('images/idle.png')
        height = self.image.get_height()
        
        # scaling the idle image
        self.new_height = self.settings.screen_heigth/6   
        self.scaling_factor = self.new_height/height 
        self.new_width =self.settings.screen_width*self.scaling_factor      
        self.image =pygame.transform.smoothscale(self.image,(int(self.new_width),int(self.new_height)))
        
        
        #setting the idle image
        self.rect = self.image.get_rect()#gets the rect of the image
        self.rect.bottomleft = (10,700)
        
        #initialize jumpimg of the dragon
        self.start_y =self.settings.screen_heigth
        self.initial_velocity = -15
        self.velocity = 0
        self.gravity = 0.8
        self.is_jumping = False
        self.on_ground = True
        
