import pygame
import sys
from pygame.sprite import Group

from screen_settings import Settings
from dragon import Dragon
from obstacles import Obstacle

class Dragon_run:
    """Dragon class"""
    def __init__(self):
        """Initializing the class."""
        pygame.init()
        
        #intializing the classes
        self.settings = Settings()
        self.dragon = Dragon()
        self.obstacles = Obstacle()
        self.group = Group()
        
        #intializing the screen
        self.screen = pygame.display.set_mode(self.settings.dimensions)
        pygame.display.set_caption("Dragon Run")
 
        #initializing the font and its font type.
        self.font=pygame.font.Font("font/TechnoRaceItalic.otf", 44)
        self.font_sys=pygame.font.Font(None,22)
        self.font_sys.set_italic(True)
      
        #initializing the tile movement.
        self.tile = False
        
        #initialising the score
        self.score_of_dragon= 0
        self.high_score=0
        
        self.running =True
        
        #initialize clock
        self.clock = pygame.time.Clock()
    
    def Main_menu(self):
        """The main menu of the game.""" 
        while True:
            #Filling the screen with colour 
            self.screen.fill((139,0,0))#Blood red colour
            
            self._text_display()
            self._image_display()
            
            #events that can be executed on the menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 

            #updating the display        
            pygame.display.flip()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.running =True
            """Main game loop"""
            while self.running:    
                #events that can be executed on the dragon game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN and not self.dragon.is_jumping:
                        if event.key == pygame.K_SPACE: #Use space bar to jump
                            self.dragon.is_jumping = True
                            self.dragon.velocity = self.dragon.initial_velocity# -15
                            self.dragon.on_ground = False
                        
                # scores the game until dragon is alive
                self.score_of_dragon =self.score_of_dragon + 1
                if self.score_of_dragon >self.high_score:
                    self.high_score =self.score_of_dragon
                    
                
                self. _jumping_checker()
                self. _On_ground_checker() 
                #Fill the screen with colour 
                self.screen.fill((128,0,128))  #white color
                
                image_dragon =self.dragon.image_mask.to_surface()
                image_obstacles=self.obstacles.image_mask.to_surface()
                
                #display the dragon and obstacle on the screen
                self.screen.blit(self.dragon.image, self.dragon.rect)
                self.screen.blit(self.obstacles.image, self.obstacles.rect)
                
                score_run=self.font_sys.render(f"Score:{self.score_of_dragon}",True,(255,255,255))
                score_rect =score_run.get_rect(center=(self.settings.screen_width // 1.11, self.settings.screen_heigth // 12))
                self.screen.blit(score_run,score_rect)
                
                high_score=self.font_sys.render(f"High Score:{self.high_score}",True,(255,255,255))
                score_rect_1 =high_score.get_rect(center=(self.settings.screen_width // 1.5 , self.settings.screen_heigth // 12))
                self.screen.blit(high_score,score_rect_1)
                
                #print(self.obstacles.rect.x,self.dragon.rect.x,self.obstacles.rect,self.dragon.rect)
                
                # Update the display
                pygame.display.flip()  
                
                self._obstacle_maintainer()
                
            
                if pygame.sprite.spritecollide(self.dragon, self.group,False,pygame.sprite.collide_mask):      
                    print("Game Over")
                    self.running =False
                    self.obstacles.rect.x =0
                    self.score_of_dragon = 0

                
                self.clock.tick(60)
    

    
    def _text_display(self):
        """Rendering the text and displaying on the screen"""
        text_title = self.font.render("Dragon Run", True, (255, 200, 10))#,(0, 0, 10))
        text_title_rect = text_title.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_heigth // 3))
        self.screen.blit(text_title,text_title_rect)
        text_instructions = self.font.render(f"Press Space to Start ", True, (255, 200, 10))#,(0, 0, 5))
        text_instructions.set_alpha(240)
        text_rect = text_instructions.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_heigth // 1.5))
        self.screen.blit(text_instructions,text_rect)
        text_instructions_1 = self.font.render(f"Press 'p' to restart after game over ", True, (255, 200, 10))#,(0, 0, 5))
        text_instructions.set_alpha(240)
        text_rect_1 = text_instructions_1.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_heigth // 1.3))
        self.screen.blit(text_instructions_1,text_rect_1)

    def _image_display(self):
        """loading and displaying the image"""
        image_of_Dragon= pygame.image.load("images/Run.png")
            
        # scaling the image
        image_of_Dragon =pygame.transform.smoothscale(image_of_Dragon,(int(self.dragon.new_width),int(self.dragon.new_height)))
            
        image_rect=image_of_Dragon.get_rect(center=((self.settings.screen_width//3,self.settings.screen_heigth//3 -5)))
        self.screen.blit(image_of_Dragon,image_rect)

    def _jumping_checker(self):
        """executes jump when spacebar is pressed and dragon is on ground"""
        if self.dragon.is_jumping and not self.dragon.on_ground:
            self.dragon.rect.y += self.dragon.velocity
            self.dragon.velocity += self.dragon.gravity

    def _On_ground_checker(self):
        """Checks if the dragon is on ground""" 
        if self.dragon.rect.bottom >= self.settings.screen_heigth:
            self.dragon.rect.bottom =self.settings.screen_heigth
            self.dragon.is_jumping =False
            self.dragon.on_ground = True
            self.dragon.velocity = 0 

    def _obstacle_maintainer(self):
        """Adds and removes the obstacle from the group"""
        if not self.tile:
            self.group.add(self.obstacles)
            self.tile = True
        
        if self.obstacles.rect.x < 0:
            self.group.remove(self.obstacles)
            self.tile = False
            
        self.obstacles.update()
        
        

if __name__ == "__main__":
    dragon_main = Dragon_run()
    dragon_main.Main_menu()
    dragon_main.run()