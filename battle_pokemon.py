import pygame, sys
from pokemon import *

'''
   Class for Pokemon specifically in Battle; Inherited from Pokemon class
   Used in Battle Scene (2 Pokemon across each other)
'''

BATTLE_POKEMON_WIDTH, BATTLE_POKEMON_HEIGHT = 200,200

class Battle_Pokemon(Pokemon):
    # str name, arr types, dict stats, arr moveset, str img, int lvl, int x, int y
    def __init__(self, name, types, stats, moveset, img, lvl, x, y):
        super().__init__(name, types, stats, moveset, img, lvl)
        self.image = pygame.transform.scale(self.image, (BATTLE_POKEMON_WIDTH, BATTLE_POKEMON_HEIGHT))
        self.x = x
        self.y = y
    
    def display(self, surface):
        surface.blit(self.image, (self.x,self.y))
