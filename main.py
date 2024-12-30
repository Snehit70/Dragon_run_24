import pygame
import sys
from pygame.sprite import Group

from screen_settings import Settings
from dragon import Dragon
from obstacles import Obstacle

class Dragon_run:
    """Dragon class"""
    def __init__(self):
        pygame.init()
        
        
        self.settings = Settings()
        self.dragon = Dragon()
        self.obstacles = Obstacle()
        self.group = Group()
        
        #intializing the screen
        self.screen = pygame.display.set_mode(self.settings.dimensions)
        pygame.display.set_caption("Dragon Run")
      
        self.tile = False
        #initialize clock
        self.clock = pygame.time.Clock()
        
        
    def run(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dragon.is_jumping = True
                        self.dragon.velocity = self.dragon.initial_velocity# -15
                        self.dragon.on_ground = False
            
            #Jumping check
            if self.dragon.is_jumping:
                self.dragon.idle_rect.y += self.dragon.velocity
                self.dragon.velocity += self.dragon.gravity
           
           #Ground collision check 
            if self.dragon.idle_rect.bottom >= self.settings.screen_heigth:
                self.dragon.idle_rect.bottom =self.settings.screen_heigth
                self.dragon.is_jumping =False
                self.dragon.on_ground = True
                self.dragon.velocity = 0  
            
 
            self.screen.fill((128,0,128))  # Fill the screen with white color
            self.screen.blit(self.dragon.idle_image_1, self.dragon.idle_rect)  # Blit the image to the screen
            self.screen.blit(self.obstacles.image, self.obstacles.rect)
            pygame.display.flip()  # Update the display
            
            
            
            #Obstacle check
            if not self.tile:
                self.group.add(self.obstacles)
                self.tile = True
            

            if self.obstacles.rect.x < 0:
                self.group.remove(self.obstacles)
                self.tile = False
                

                
            print(len(self.group))
            
            self.obstacles.update()
            
            
            self.clock.tick(60)
        

if __name__ == "__main__":
    dragon_main = Dragon_run()
    dragon_main.run()