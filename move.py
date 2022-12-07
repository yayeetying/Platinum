import pygame, sys, random

'''
   Move class
   Example of move 'Scratch':
      self.move_name = 'Scratch'
      self.type = 'Attack' (or Buff, Debuff)
      self.attack_power = 60 (or 1x = Increase/Decrease <Attack> by 1x)
      self.involved_stat = 'Attack'
      self.move_type = 'Normal'

'''

def calculate_damage(poke_level, move_power, a_stat, d_stat):
    factor = random.uniform(0.85, 1)
    return int((((2 * poke_level / 5 + 2) * move_power * a_stat/d_stat) / 50 + 2) * factor)

class Move():
    def __init__(self, move_name, type, attack_power, involved_stat, move_type):
        super().__init__()
        self.move_name = move_name
        self.type = type
        self.attack_power = attack_power
        self.involved_stat = involved_stat
        self.move_type = move_type

        '''
        # For Animation
        self.time = 0
        if self.type == 'Attack':
            self.image = 'images/move_effects/scratch.png'
        elif self.type == 'Buff':
            print('lol') # No Pokemon have Buff moves yet
            self.image = 'images/move_effects/debuff.png'
        else: #Debuff
            self.image = 'images/move_effects/debuff.png'
        '''

    # 3 Types of Moves: Attacking, Buffing (self), Debuffing (opponent)
    def execute_move(self, player_pokemon, opponent_pokemon):
        if self.type == 'Attack':
            if self.involved_stat == 'Attack': 
                damage = calculate_damage(player_pokemon.level, self.attack_power, player_pokemon.current_stats['Attack'], opponent_pokemon.current_stats['Defense'])
                opponent_pokemon.lose_hp(damage)
            else: #'SpAtk'
                damage = calculate_damage(player_pokemon.level, self.attack_power, player_pokemon.current_stats['SpAtk'], opponent_pokemon.current_stats['SpDef'])
                opponent_pokemon.lose_hp(damage)
        elif self.type == 'Buff':
            print('lol') # No Pokemon have Buff moves yet
        else: # Debuff
            opponent_pokemon.current_stats[self.involved_stat] = opponent_pokemon.current_stats[self.involved_stat] - self.attack_power
    
    '''
    def animate_move(self, surface, x, y):
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (100, 100))
        surface.blit(img, (x,y))
    '''

