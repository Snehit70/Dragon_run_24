import pygame

from screen_settings import Settings

class Dragon:
    """A class for dragon and its functions."""
    
    def __init__(self):
        """Initializing dragon class."""
        
        self.settings = Settings()
        
        self.idle_image = pygame.image.load('images/idle.png')
        height = self.idle_image.get_height()
        
        # scaling the idle image
        self.new_height = self.settings.screen_heigth/6   
        self.scaling_factor = self.new_height/height 
        self.new_width =self.settings.screen_width*self.scaling_factor      
        self.idle_image_1 =pygame.transform.smoothscale(self.idle_image,(int(self.new_width),int(self.new_height)))
        
        
        #setting the idle image
        self.idle_rect = self.idle_image_1.get_rect()#gets the rect of the image
        self.idle_rect.bottomleft = (0,self.settings.screen_heigth)
        
        #initialize jumpimg of the dragon
        self.start_y =self.settings.screen_heigth
        self.initial_velocity = -15
        self.velocity = 0
        self.gravity = 0.8
        self.is_jumping = False
        self.on_ground = True
        
if __name__ == "__main__":
    dragon = Dragon()
    dragon.run() 