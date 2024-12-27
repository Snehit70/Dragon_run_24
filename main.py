import pygame
import sys

class Dragon:
    """Dragon class"""
    def __init__(self):
        pygame.init()
        
        #screen dimensions
        self.screen_width=800
        self.screen_heigth=400
        self.dimensions=(self.screen_width,self.screen_heigth)
        
        #intializing the screen
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption("Dragon Run")
        print("Pygame window initialized")
        
        #initialize clock
        self.clock = pygame.time.Clock()
        
        #loading the images
        self.idle_image = pygame.image.load('images/idle.png')
        self.tile =pygame.image.load('images/block_tiles_red.png')
        height = self.idle_image.get_height()
        height_tile =self.tile.get_height()
        print(self.tile.get_width())
        
        #initialize jumpimg of the dragon
        self.start_y =self.screen_heigth
        self.initial_velocity = -15
        self.velocity = 0
        self.gravity = 0.8
        self.is_jumping = False
        self.on_ground = True
               
        #scaling the images.
        self.new_height = self.screen_heigth/6
        
        self.new_height_tile = self.screen_heigth/12
        
        self.scaling_factor = self.new_height/height
        
        self.scaling_factor_tile = self.new_height_tile/height_tile
        
        self.new_width =self.screen_width*self.scaling_factor
        
        self.new_width_tile =self.screen_width/36
        
        self.idle_image_1 =pygame.transform.smoothscale(self.idle_image,(int(self.new_width),int(self.new_height)))
        
        self.tile_1 =pygame.transform.smoothscale(self.tile,(int(self.new_width_tile),int(self.new_height_tile)))
        
        #setting the idle image
        self.idle_rect = self.idle_image_1.get_rect()#gets the rect of the image
        self.idle_rect.bottomleft = (0,self.screen_heigth)

        #setting the tile
        self.tile_rect = self.tile_1.get_rect()
        self.tile_rect.bottomleft = (100,self.screen_heigth)
        
    def run(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.is_jumping = True
                        self.velocity = self.initial_velocity
                        self.on_ground = False
            
            #Jumping check
            if self.is_jumping:
                self.idle_rect.y += self.velocity
                self.velocity += self.gravity
           
           #Ground collision check 
            if self.idle_rect.bottom >= self.screen_heigth:
                self.idle_rect.bottom =self.screen_heigth
                self.is_jumping =False
                self.on_ground = True
                self.velocity = 0  
            
            self.screen.fill((128,0,128))  # Fill the screen with white color
            self.screen.blit(self.idle_image_1, self.idle_rect)  # Blit the image to the screen
            self.screen.blit(self.tile_1, self.tile_rect)
            pygame.display.flip()  # Update the display
            self.clock.tick(60)

    def dragon_scaling():
        pass
        

if __name__ == "__main__":
    dragon = Dragon()
    dragon.run()