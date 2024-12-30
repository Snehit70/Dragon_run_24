import pygame

class Settings:
    """ A settings class for all the screen settings."""
    
    def __init__(self):
        """Inititalizing settings."""
        
        #screen dimensions
        self.screen_width=800
        self.screen_heigth=400
        self.dimensions=(self.screen_width,self.screen_heigth)