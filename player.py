import pygame, sys

'''
   Player class
'''

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Player variables
        self.width = 80
        self.height = 70
        self.speed = 5 # Deals with xy movement speed

        # Arrays contain walking frames
        self.left = self.populate_walking("left")
        self.right = self.populate_walking("right")
        self.up = self.populate_walking("up")
        self.down = self.populate_walking("down")
        self.sprites = self.down # Current walking sprites
        
        self.is_animating = False
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.pos_x = x
        self.pos_y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    # Update sprite animation (next frame)
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.15

            # Restart animation
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
            self.rect.topleft = [self.pos_x, self.pos_y]
            self.is_animating = False

    def update_x(self, value):
        self.pos_x += value
    
    def update_y(self, value):
        self.pos_y += value

    # Helper function to populate walking sprite arrays 
    def populate_walking(self, direction):
        frames = []
        for num in range(1,5):
            img = pygame.image.load("images/dawn/{}{}.png".format(direction, num))
            img = pygame.transform.scale(img, (self.width, self.height))
            frames.append(img)
        return frames