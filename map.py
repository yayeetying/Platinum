import pygame, sys

'''
   Map class
   Generates objects of different routes given .txt file
'''
ELEMENT_WIDTH, ELEMENT_HEIGHT = 80,90

def load_element(path):
    element = pygame.image.load(path)
    element = pygame.transform.scale(element, (ELEMENT_WIDTH, ELEMENT_HEIGHT))
    return element

# Load images to be used
tree_dark = load_element("images/map_scenery/tree_dark.png")
tree_light = load_element("images/map_scenery/tree_light.png")
grass_big = load_element("images/map_scenery/grass_big.png")
grass_small = load_element("images/map_scenery/grass_small.png")
flower_yellow = load_element("images/map_scenery/flower_yellow.png")
flower_purple = load_element("images/map_scenery/flower_purple.png")
water_dark = load_element("images/map_scenery/water_dark.png")
water_light = load_element("images/map_scenery/water_light.png")
dirt_path = load_element("images/map_scenery/dirt_path.png")
sand_path = load_element("images/map_scenery/sand_path.png")

class Map():
    def __init__(self, txt_file):
        super().__init__()

        self.char_map = self.read_file(txt_file)
        self.neighbors = [] # Places that can be entered from this map

    # Given .txt file, return 2D array of file
    def read_file(self, txt_file):
        row = []
        with open(txt_file, 'r') as f:
            for line in f:
                col = []
                for char in line:
                    if char != '\n':
                        col.append(char)
                row.append(col)
        return row

    # Load maps
    def display(self, surface):
        # Top-left (x,y) cords of tile/patch
        x,y = 0,0
        for row in self.char_map:
            for char in row: 
                # Switch statement for different tiles
                match char:
                    case '#':
                        surface.blit(tree_dark, (x,y))
                    case '@':
                        surface.blit(tree_light, (x,y))
                    case '.':
                        surface.blit(grass_big, (x,y))
                    case ',':
                        surface.blit(grass_small, (x,y))
                    case '0':
                        surface.blit(dirt_path, (x,y))
                    case '1':
                        surface.blit(sand_path, (x,y))
                    case '2':
                        surface.blit(water_light, (x,y))
                    case '3':
                        surface.blit(water_dark, (x,y))
                    case 'a':
                        surface.blit(flower_yellow, (x,y))
                    case 's':
                        surface.blit(flower_purple, (x,y))
                x += 50
            x = 0
            y += 50