import pygame, sys
from pokemon import *

'''
   Class for Pokemon specifically in Battle; Inherited from Pokemon class
   Used in Battle Scene (2 Pokemon across each other)
'''

BATTLE_POKEMON_WIDTH, BATTLE_POKEMON_HEIGHT = 200,200

class Battle_Pokemon(Pokemon):
    def __init__(self, Pokemon, x, y, width = BATTLE_POKEMON_WIDTH, height = BATTLE_POKEMON_HEIGHT):
        super().__init__(Pokemon.name, Pokemon.types, Pokemon.stats, Pokemon.moveset, Pokemon.image, Pokemon.level)
        self.image = self.load_image()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        '''
        self.current_stats = 
        self.is_dead =
        '''
    
    def display(self, surface):
        surface.blit(self.image, (self.x,self.y))
