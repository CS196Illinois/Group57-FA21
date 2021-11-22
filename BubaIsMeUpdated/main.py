# BubaIsMe
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standard
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    #K_ESCAPE,
    KEYDOWN#,
    #QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640

# Initialize pygame
pygame.init()

def move(block_to_move, pressed_keys):
        if block_to_move.is_push and (not block_to_move.is_stop):
            if pressed_keys[K_UP]:
                block_to_move.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                block_to_move.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                block_to_move.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                block_to_move.rect.move_ip(5, 0)

            # Keep the block on the screen
            if block_to_move.rect.left < 0:
                block_to_move.rect.left = 0
            if block_to_move.rect.right > SCREEN_WIDTH:  # SCREEN_WIDTH is defined outside the game loop
                block_to_move.rect.right = SCREEN_WIDTH
            if block_to_move.rect.top <= 0:
                block_to_move.rect.top = 0
            if block_to_move.rect.bottom >= SCREEN_HEIGHT:  # SCREEN_HEIGHT is defined outside the game loop
                block_to_move.rect.bottom = SCREEN_HEIGHT
# Parent Block Class
class Block(pygame.sprite.Sprite):
    def __init__(self, set_x, set_y, set_type, set_is_you, set_can_push,
                 set_is_win, set_is_stop, set_image):
        super(Block, self).__init__()
        self.dimension = (64, 64)
        self.x = set_x
        self.y = set_y
        self.type = set_type
        self.is_you = set_is_you
        self.can_push = set_can_push
        self.is_win = set_is_win
        self.is_stop = set_is_stop
        self.surf = pygame.image.load(set_image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    # Move blocks based on pressed_keys
    # pressed_keys is defined in the game loop and is a set of the keys pressed
    


# Object class
class Object(Block):
    def __init__(self, set_x, set_y, set_is_you, set_can_push, set_is_win,
                 set_is_stop, set_image):
        super().__init__(set_x, set_y, "Object", set_is_you, set_can_push,
                         set_is_win, set_is_stop, set_image)


# Variable Class
class Variable(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Variable", False, True, False, True,
                         set_image)


# Attribute Class
class Attribute(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Attribute", False, True, False, True,
                         set_image)


# Operator Class
class Operator(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Operator", False, True, False, True,
                         set_image)

has_won = False
block_array = []
while (not has_won):
	for event in pygame.event.get():
		if (event.type == KEYDOWN):
			for i in range(block_array):
				if (block_array[i].can_move == True):
					move(block_array[i])

