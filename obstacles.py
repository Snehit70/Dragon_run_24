import pygame
from pygame.sprite import Sprite, Group

from screen_settings import Settings

class Obstacle(Sprite):
    """A class for all the obstacles for dragon."""
    
    def __init__(self):
        """Initializing the obstacles class."""
        super().__init__()
               
        self.settings = Settings()
                
        #loading the images
        self.image =pygame.image.load('images/block_tiles_red.png')#for sprite.
        height_tile =self.image.get_height()

        #scaling the images.
        self.new_height_tile = self.settings.screen_heigth/12        
        self.scaling_factor_tile = self.new_height_tile/height_tile      
        self.new_width_tile =self.settings.screen_width/36       
        self.image =pygame.transform.scale(self.image,(int(self.new_width_tile),int(self.new_height_tile)))
        
        #setting the tile
        self.rect = self.image.get_rect()#for sprite
        self.rect.bottomleft = (self.settings.screen_width-self.settings.screen_width/16,self.settings.screen_heigth)#for sprite.

    def update(self):
        """Updating the position of the obstacle."""
        self.rect.x -= 10
        
        if self.rect.x <= 0:
            self.rect.x = self.settings.screen_width
 