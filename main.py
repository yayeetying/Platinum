import pygame
import sys
from player import *
from trainer import *
from tile import *
from map import *
from pokemon import *
from pokemon import *
from battle_pokemon import *
from move import *

'''
   Remake of the Pokemon Platinum game
   Make sure user runs while inside the Platinum repository
'''

pygame.init()

WIDTH, HEIGHT = 1400, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Platinum")

# Load player object
player = Player(400,220)

# Load necessary background images
battle_grass = load_element("images/battle_backgrounds/battle_grass.png", WIDTH, HEIGHT)

# Dictionary of all NPC trainers (key: name; value = Trainer object)
NPC_trainers = {}

# Controls which screens to show: -1 = choosing Pokemon; 0 = map; 1 = battle
global GAME_STATE 
BATTLE_PLAYER_X, BATTLE_PLAYER_Y = 150, 375
BATTLE_OPPONENT_X, BATTLE_OPPONENT_Y = 1050, 125
BATTLE_PLAYER_SIZE = 350

# For battling state
global current_pokemon 
global opponent_pokemon

# Defines FPS game runs on
FPS = 60

# For background of a button
def draw_rectangle(color, x, y, width, height):
    pygame.draw.rect(WIN, color, pygame.Rect(x, y, width, height))

# Display text; x,y cords given are center x,y cords
def print_text(text, color, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    WIN.blit(text, textRect)

def choose_Pokemon(choice):
    if choice == 'Chimchar':
        starter_pokemon = Pokemon('Chimchar', ['Fire'], {'HP': 22, 'Attack': 58, 'Defense': 44, 'SpAtk': 58, 'SpDef': 44, 'Speed': 61}, ['Scratch', 'Leer'], 'images/pokemon/chimchar.png', 5)
        opponent_pokemon = Pokemon('Piplup', ['Water'], {'HP': 26, 'Attack': 51, 'Defense': 53, 'SpAtk': 61, 'SpDef': 56, 'Speed': 40}, ['Pound', 'Growl'], 'images/pokemon/piplup.png', 5)
    elif choice == 'Piplup':
        starter_pokemon = Pokemon('Piplup', ['Water'], {'HP': 26, 'Attack': 51, 'Defense': 53, 'SpAtk': 61, 'SpDef': 56, 'Speed': 40}, ['Pound', 'Growl'], 'images/pokemon/piplup.png', 5)
        opponent_pokemon = Pokemon('Turtwig', ['Grass'], {'HP': 28, 'Attack': 68, 'Defense': 64, 'SpAtk': 45, 'SpDef': 55, 'Speed': 31}, ['Tackle', 'Leer'], 'images/pokemon/turtwig.png', 5)
    else:
        starter_pokemon = Pokemon('Turtwig', ['Grass'], {'HP': 28, 'Attack': 68, 'Defense': 64, 'SpAtk': 45, 'SpDef': 55, 'Speed': 31}, ['Tackle', 'Leer'], 'images/pokemon/turtwig.png', 5)
        opponent_pokemon = Pokemon('Chimchar', ['Fire'], {'HP': 22, 'Attack': 58, 'Defense': 44, 'SpAtk': 58, 'SpDef': 44, 'Speed': 61}, ['Scratch', 'Leer'], 'images/pokemon/chimchar.png', 5)
    
    NPC_trainers['Barry'].add_Pokemon(opponent_pokemon)
    player.Pokemon.append(starter_pokemon)

def draw_choice():
    # Draw white screen to erase previous drawings
    draw_rectangle("white", 0, 0, WIDTH, HEIGHT)
    print_text("Choose a Starter Pokemon!", 'darkturquoise', WIDTH // 2, 100)
    # Draw buttons and text for options
    draw_rectangle("red", WIDTH/7, 200, WIDTH/7+50, 100)
    draw_rectangle("blue", 3 * WIDTH/7, 200, WIDTH/7+50, 100)
    draw_rectangle("green", 5 * WIDTH/7, 200, WIDTH/7+50, 100)
    # Alignment Math: x || y + (width || height) / 2
    print_text("Chimchar", 'black', WIDTH/7 + WIDTH/14 + 25, 250)
    print_text("Piplup", 'black', 3 * WIDTH/7 + WIDTH/14 + 25, 250)
    print_text("Turtwig", 'black', 5 * WIDTH/7 + WIDTH/14 + 25, 250)
    pygame.display.flip()

# Draws map background
def draw_map(map_file):
    # Draw bed of green as default
    draw_rectangle("forestgreen", 0, 0, WIDTH, HEIGHT)

    map = Map(map_file)  # Map object
    map.display(WIN)
    return map

# Returns 0 if still in map; 1 if in battle mode
def map_state(player, moving_sprites):
    # Ensures smooth player movement
    keys_pressed = pygame.key.get_pressed()

    # Simulate animated player
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
        player.is_animating = True 

    if keys_pressed[pygame.K_LEFT]:
        player.update_x(-1 * player.speed)
    elif keys_pressed[pygame.K_RIGHT]:
        player.update_x(player.speed)
    elif keys_pressed[pygame.K_UP]:
        player.update_y(-1 * player.speed)
    elif keys_pressed[pygame.K_DOWN]:
        player.update_y(player.speed)
    
    # Drawing
    map = draw_map('maps/test.txt')
    moving_sprites.draw(WIN)
    moving_sprites.update()
    state = map.map_collision(player)
    pygame.display.flip()

    return state # Updates GAME_STATE

# Draws battle background
def draw_battle():
    WIN.blit(battle_grass, (0,0))

# Draw battle background and have player interact with it
#def battle_state(surface, player_pokemon, opponent_pokemon):
def battle_state(surface, c_pokemon, o_pokemon):
    opponent_turn = False
    while c_pokemon.current_stats['HP'] > 0 and o_pokemon.current_stats['HP'] > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP: # Battle; Click in battles
                mouse = pygame.mouse.get_pos()
                #print(str(mouse[0]) + "," + str(mouse[1]))
                if button_clicked(mouse, 600, 500, 900, 600): # Move 1
                    move_name = player.Pokemon[0].moveset[0]
                    move1 = create_move(move_name)
                    move1.execute_move(c_pokemon, o_pokemon)
                    #move1.animate_move(WIN, 1150, 250) # Animate onto the opponent
                    opponent_turn = True
                elif button_clicked(mouse, 1000, 500, 1300, 600): # Move 2
                    move_name = player.Pokemon[0].moveset[1]
                    move2 = create_move(move_name)
                    move2.execute_move(c_pokemon, o_pokemon)
                    #move1.animate_move(WIN, 1150, 250)
                    opponent_turn = True

        if opponent_turn == True:
            if random.random() < 0.5:
                num = 0
            else:
                num = 1
            move_name = NPC_trainers['Barry'].Pokemon[0].moveset[num]
            move1 = create_move(move_name)
            move1.execute_move(o_pokemon, c_pokemon)
            #move1.animate_move(WIN, 300, 550) # Animate onto the player's Pokemon
            print("Player: " + str(current_pokemon.current_stats))
            print("Opponent: " + str(opponent_pokemon.current_stats))
            opponent_turn = False

        draw_battle()
        c_pokemon.display(surface)
        o_pokemon.display(surface)
        draw_stats(c_pokemon, BATTLE_PLAYER_X+25, BATTLE_PLAYER_Y-100)
        draw_stats(o_pokemon, BATTLE_OPPONENT_X-45, BATTLE_OPPONENT_Y-100)
        draw_moves(c_pokemon)
        pygame.display.flip()
    
    return True # Go back to the Map

def draw_stats(pokemon, x, y):
    draw_rectangle('palegreen', x, y, 300, 100)
    print_text(str(pokemon.name), 'black', x + 70, y+30)
    print_text('Lv.' + str(pokemon.level), 'black', x + 250, y+30)

def draw_moves(pokemon):
    draw_rectangle('forestgreen', 650, 350, 600, 100)
    print_text('What will ' + str(pokemon.name) + ' do?', 'honeydew', 950, 400)

    for num in range(len(pokemon.moveset)):
        draw_rectangle('forestgreen', 600 + 400 * num, 500, 300, 100)
        print_text(str(pokemon.moveset[num]), 'honeydew', 750 + 400 * num, 550)
        if num >= 2:
            draw_rectangle('forestgreen', 600 + 400 * (num-2), 650, 300, 100)
            print_text(str(pokemon.moveset[num]), 'honeydew', 750 + 400 * (num-2), 700)

# Handles main loop
def main():
    clock = pygame.time.Clock()

    # Add trainers to NPC_trainers dictionary once
    NPC_rival = Trainer('Barry', 200, 200)
    NPC_trainers.update({'Barry': NPC_rival})

    # Create moving sprites and group them together
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)

    # For battling state
    global current_pokemon 
    global opponent_pokemon

    GAME_STATE = -1

    run = True
    while run:
        clock.tick(FPS) # Control speed of game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if GAME_STATE == -1 and event.type == pygame.MOUSEBUTTONUP: # Choose Pokemon; Detect if any button is clicked
                mouse = pygame.mouse.get_pos()
                if button_clicked(mouse, WIDTH/7, 200, 2 * WIDTH/7 + 50, 300):
                    choose_Pokemon('Chimchar')
                    GAME_STATE = 0
                elif button_clicked(mouse, 3 * WIDTH/7, 200, 4 * WIDTH/7 + 50, 300):
                    choose_Pokemon('Piplup')
                    GAME_STATE = 0
                elif button_clicked(mouse, 5 * WIDTH/7, 200, 6 * WIDTH/7 + 50, 300):
                    choose_Pokemon('Turtwig')
                    GAME_STATE = 0
            elif GAME_STATE == 0 and event.type == pygame.KEYDOWN:  # Map; Change direction of sprites in map state
                if event.key == pygame.K_LEFT:
                    player.sprites = player.left
                    player.current_direction = "left"
                elif event.key == pygame.K_RIGHT:
                    player.sprites = player.right
                    player.current_direction = "right"
                elif event.key == pygame.K_UP:
                    player.sprites = player.up
                    player.current_direction = "up"
                elif event.key == pygame.K_DOWN:
                    player.sprites = player.down
                    player.current_direction = "down"
        
        if GAME_STATE == -1: # Choose Pokemon State
            draw_choice()
        elif GAME_STATE == 0: # Map State
            GAME_STATE = map_state(player, moving_sprites)
        elif GAME_STATE == 1: # Battle State
            current = player.Pokemon[0]
            current_pokemon = Battle_Pokemon(current, BATTLE_PLAYER_X, BATTLE_PLAYER_Y, BATTLE_PLAYER_SIZE, BATTLE_PLAYER_SIZE)

            opponent = NPC_trainers['Barry'].Pokemon[0]
            opponent_pokemon = Battle_Pokemon(opponent, BATTLE_OPPONENT_X, BATTLE_OPPONENT_Y)
            
            quit = battle_state(WIN, current_pokemon, opponent_pokemon)
            if quit == False:
                run = False
            else: # True
                '''
                # Reset stats after battle to regular stats
                current_pokemon.current_stats = current_pokemon.stats
                opponent_pokemon.current_stats = opponent_pokemon.stats
                '''
                GAME_STATE = 0 # Return to Map State
        
    pygame.quit()

# Given mouse cords, top-left cords and bottom-right cords of a rectangle, detect clicking
def button_clicked(mouse, top_x, top_y, bottom_x, bottom_y):
    return top_x <= mouse[0] <= bottom_x and top_y <= mouse[1] <= bottom_y

# Given name of move, create Move object
def create_move(name):
    match name:
        case 'Scratch':
            return Move(name, 'Attack', 40, 'Attack', 'Normal')
        case 'Tackle':
            return Move(name, 'Attack', 45, 'Attack', 'Normal')
        case 'Pound':
            return Move(name, 'Attack', 35, 'Attack', 'Normal')
        case 'Leer':
            return Move(name, 'Debuff', 5, 'Defense', 'Normal')
        case 'Growl':
            return Move(name, 'Debuff', 5, 'Attack', 'Normal')

    return None # Need to make new move

if __name__ == "__main__":
    main()

