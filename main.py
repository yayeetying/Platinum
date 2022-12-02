import pygame, sys 
from player import *
from map import *
from pokemon import *
from battle_pokemon import *

'''
   Remake of the Pokemon Platinum Game
   Make sure user runs while inside the Platinum repository
'''

WIDTH, HEIGHT = 1400, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Platinum")

# 0 = map; 1 = battle
global GAME_STATE

# Defines FPS game runs on
FPS = 60

def draw_map():
    # Draw bed of green as default
    pygame.draw.rect(WIN, "forestgreen", pygame.Rect(0,0,1400,800))

    route_201 = Map('maps/test.txt') # Map object
    route_201.display(WIN)

# Handles main loop
def main():
    clock = pygame.time.Clock()

    # Create moving sprites and group them together
    moving_sprites = pygame.sprite.Group()
    player = Player(100,100)
    moving_sprites.add(player)

    GAME_STATE = 0

    run = True
    while run:
        clock.tick(FPS) # Control speed of game

        if GAME_STATE == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN: # Change direction of sprites
                    if event.key == pygame.K_LEFT:
                        player.sprites = player.left
                    elif event.key == pygame.K_RIGHT:
                        player.sprites = player.right
                    elif event.key == pygame.K_UP:
                        player.sprites = player.up
                    elif event.key == pygame.K_DOWN:
                        player.sprites = player.down

            # Ensures smooth player movement
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_LEFT]:
                player.update_x(-1 * player.speed)
            elif keys_pressed[pygame.K_RIGHT]:
                player.update_x(player.speed)
            elif keys_pressed[pygame.K_UP]:
                player.update_y(-1 * player.speed)
            elif keys_pressed[pygame.K_DOWN]:
                player.update_y(player.speed)
            elif keys_pressed[pygame.K_SPACE]:
                GAME_STATE = 1
            
            # Simulate animated player
            if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
                player.is_animating = True 
            
            # Drawing
            draw_map()
            moving_sprites.draw(WIN)
            moving_sprites.update()
            pygame.display.flip()
        
        elif GAME_STATE == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            chimchar = Battle_Pokemon('Chimchar', ['Fire'], {'Attack': 5}, ['Scratch', 'Leer'], 'images/pokemon/chimchar.png', 5, 100, 100)
            chimchar.display(WIN)
            pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()

