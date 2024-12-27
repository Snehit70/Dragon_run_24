import pygame
import sys

class Dragon:
    """Dragon class"""
    def __init__(self):
        pygame.init()
        
        #screen dimensions
        self.screen_width=1200
        self.screen_heigth=800
        self.dimensions=(self.screen_width,self.screen_heigth)
        
        #intializing the screen
        self.screen = pygame.display.set_mode(self.dimensions)
        print("Pygame window initialized")
        
        #loading the images
        self.idle_image = pygame.image.load('images/idle.png')
        height=self.idle_image.get_height()
        width =self.idle_image.get_width()
        
        #scaling the images.
        self.new_height = self.screen_heigth/8
        self.scaling_factor = self.new_height/height
        self.new_width =self.screen_width*self.scaling_factor
        self.idle_image_1 =pygame.transform.smoothscale(self.idle_image,(int(self.new_width),int(self.new_height)))
        
        #setting the idle image
        self.idle_rect = self.idle_image_1.get_rect()#gets the rect of the image
        self.idle_rect.bottomleft = (0,self.screen_heigth)

    def run(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill((128,0,128))  # Fill the screen with white color
            self.screen.blit(self.idle_image_1, self.idle_rect)  # Blit the image to the screen
            pygame.display.flip()  # Update the display

    def dragon_scaling():
        pass
        

if __name__ == "__main__":
    dragon = Dragon()
    dragon.run()