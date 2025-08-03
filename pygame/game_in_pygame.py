# Import necessary libraries
import pygame
from pygame.locals import * 

pygame.init()

# colour's
class Colour:
    def __init__(self):
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

colour = Colour()

# screen hight and width
screen_width = 800
screen_height = 600
screen_size = (screen_width,screen_height)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("platformer") # name the window

# player

player_x = 400
player_y = 300

player_width = 75
player_height = 75

player_speed = 150
player_gravity = 10

player = pygame.image.load('Python/pygame/why.png').convert()  # player image

player_scaled = pygame.transform.scale(player, (player_width, player_height))

player_rect = player.get_rect() # player rect gotten by the image

# platform

platform_x = 300
platform_y = 500

platform_width = 400
platform_height = 50

platform = pygame.image.load('Python/pygame/grass.png').convert() # platform image

platform_scaled =  pygame.transform.scale(platform, (platform_width, platform_height))

platform_rect = platform.get_rect()

# clock or frame rate
clock = pygame.time.Clock()
tick_speed = 60

delta_time = 0.1

# game loop 
game_running = True
while game_running :
    
    

    for event in pygame.event.get():
        
        # To make the X button valid
        if event.type == QUIT:
            print('Game stopped')
            game_running = False


    # player_gravity 
    player_y += player_gravity
     
    # player movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed * delta_time
    if keys[K_RIGHT]:
        player_x += player_speed * delta_time
    if keys[K_UP]:
        player_y -= player_speed * delta_time
   
   # collison
    if player_rect.colliderect(platform_rect):
        player_gravity = 0
        print("collision")
    else:
        player_gravity = 10
   
    # items that are being draw
    
    screen.fill(colour.black) # background colour is black
    
    screen.blit(platform_scaled, (platform_x, platform_y)) # draws the platform
    
    screen.blit(player_scaled, (player_x, player_y)) # draws the player on the screen
    

    delta_time = clock.tick(tick_speed) / 1000 # clock in the game
    delta_time = max(0.001, min(0.1, delta_time))
    
    # this updates the game
    # pygame.display.update() # updates part of screen if specified
    pygame.display.flip() # updates the full screen
    

    
pygame.quit() # to make a clean quit