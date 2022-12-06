import pygame, sys

'''
   Pokemon class
'''

class Pokemon(pygame.sprite.Sprite):
    # str name, arr types, dict stats, arr moveset, str img, int lvl
    def __init__(self, name, types, stats, moveset, img, lvl):
        super().__init__()

        # Pokemon variables: name, type1, type2, stats(HP, attack, defense, spattack, spdefense, speed), moveset(move1, move2, move3, move4), img, lvl
        self.name = name
        self.types = types # Secondary type is optional
        self.stats = stats
        self.moveset = moveset
        self.image = img # String path to img
        self.level = lvl

    def load_image(self):
        return pygame.image.load(self.image)
        

