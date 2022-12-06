import pygame, sys

'''
   Move class
   Example of move 'Scratch':
      self.move_name = 'Scratch'
      self.type = 'Attack' (or Buff, Debuff)
      self.attack_power = 60 (or 1x = Increase/Decrease <Attack> by 1x)
      self.involved_stat = 'Attack'
      self.move_type = 'Normal'

'''

class Move():
    def __init__(self, move_name, type, attack_power, involved_stat, move_type):
        super().__init__()
        self.move_name = move_name
        self.type = type
        self.attack_power = attack_power
        self.involved_stat = involved_stat
        self.move_type = move_type

    # 3 Types of Moves: Attacking, Buffing (self), Debuffing (opponent)
    def execute_move(self, player_pokemon, opponent_pokemon):
        if self.type == 'Attack':
            if self.involved_stat == 'Attack':
                
            else: # Involved stat is SpAtk

        elif self.type == 'Buff':
        else: # Debuff


