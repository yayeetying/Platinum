import pygame, sys

'''
   Tile class
   Generates singular tile for maps
'''

def load_element(path, width, height):
    element = pygame.image.load(path)
    element = pygame.transform.scale(element, (width, height))
    return element

class Tile():
    def __init__(self, char, x, y):
        self.width, self.height = 80,90
        self.x, self.y = x,y
        self.char = char
        self.image_path = self.convert(char)

    # Given char, return a certain image path (str)
    def convert(self, char):
        match char:
            case '#':
                return "images/map_scenery/tree_dark.png"
            case '@':
                return "images/map_scenery/tree_light.png"
            case '.':
                return "images/map_scenery/grass_big.png"
            case ',':
                return "images/map_scenery/grass_small.png"
            case 'a':
                return "images/map_scenery/flower_yellow.png"
            case 's':
                return "images/map_scenery/flower_purple.png"
            case '3':
                return "images/map_scenery/water_dark.png"
            case '2':
                return "images/map_scenery/water_light.png"
            case '0':
                return "images/map_scenery/dirt_path.png"
            case '1':
                return "images/map_scenery/sand_path.png"

    def display(self, surface):
        element = load_element(self.image_path, self.width, self.height)
        surface.blit(element, (self.x, self.y))

    # Detect collision based on player's xy cords
    def collision(self, player_x, player_y):
        if self.x <= player_x and player_x <= self.x + self.width and self.y <= player_y and player_y <= self.y + self.height:
            return True
        return False