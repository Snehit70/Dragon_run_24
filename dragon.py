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
        self.new_height = 120 
        self.scaling_factor = self.new_height/height 
        self.new_width =80     
        self.image =pygame.transform.smoothscale(self.image,(int(self.new_width),int(self.new_height)))
        
        
        #setting the idle image
        self.rect = self.image.get_rect()#gets the rect of the image
        self.rect.bottomleft = (0,720)
        
        self.image_mask =pygame.mask.from_surface(self.image)
        #initialize jumpimg of the dragon
        self.start_y =self.settings.screen_heigth
        self.initial_velocity = -15
        self.velocity = 0
        self.gravity = 0.8
        self.is_jumping = False
        self.on_ground = True
        
