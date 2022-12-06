import pygame, sys

'''
   Trainer class - keeps track of all NPC Trainers
'''

class Trainer(pygame.sprite.Sprite):
    def __init__(self, name, x, y, Pokemon=[]):
        super().__init__()
        # Player variables
        self.name = name
        self.width = 80
        self.height = 70
        self.Pokemon = Pokemon # Array of Pokemon objects
        self.x = x
        self.y = y

    def add_Pokemon(self, monster):
        self.Pokemon.append(monster)

