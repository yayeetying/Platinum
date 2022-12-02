import pygame, sys

'''
   Pokemon class
'''

class Pokemon(pygame.sprite.Sprite):
    # str name, arr types, dict stats, arr moveset, str img, int lvl
    def __init__(self, name, types, stats, moveset, img, lvl):
        super().__init__()

        # Pokemon variables: name, type1, type2, stats(attack, defense, spattack, spdefense, speed), moveset(move1, move2, move3, move4), img, lvl
        self.name = name
        self.type1 = types[0]
        if len(types) == 2:
            self.type2 = types[1] # Secondary type; optional
        self.stats = stats
        self.moveset = moveset
        self.image = pygame.image.load(img)
        self.level = lvl
        

