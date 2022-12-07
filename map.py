import pygame, sys, random
from tile import *

'''
   Map class
   Generates different routes given .txt file
   Each route is a 2D array of Tiles
'''

SPAWN_RATE = 0.003
#SPAWN_RATE = 0

class Map():
    def __init__(self, txt_file):
        super().__init__()

        self.char_map = self.read_file(txt_file) # 2D array
        self.neighbors = [] # Places that can be entered from this map

    # Given .txt file, return 2D array of file
    def read_file(self, txt_file):
        x,y = 0,0
        row = []
        with open(txt_file, 'r') as f:
            for line in f:
                col = []
                for char in line:
                    if char != '\n':
                        tile = Tile(char, x, y)
                        col.append(tile)
                        x += 50
                row.append(col)
                x = 0
                y += 50
        return row

    # Load maps
    def display(self, surface):
        for row in self.char_map:
            for tile in row:
                tile.display(surface)

    def map_collision(self, player):
        for row in self.char_map:
            for tile in row:
                if tile.collision(player.pos_x, player.pos_y):
                    if tile.char == '#' or tile.char == '@' or tile.char == '3' or tile.char == '2': # Trees and Water; cannot walk through
                        if player.current_direction == "right":
                            player.update_x(-1 * player.speed)
                        elif player.current_direction == "left":
                            player.update_x(player.speed)
                        elif player.current_direction == "up":
                            player.update_y(player.speed)
                        elif player.current_direction == 'down':
                            player.update_y(-1 * player.speed)
                    elif (tile.char == '.' or tile.char == ',') and random.random() < SPAWN_RATE:
                        return 1
                    elif tile.char == 'a' or tile.char == 's':
                        return 0
        return 0
    