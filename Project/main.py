# Import pygame
import pygame
from pygame.constants import WINDOWEXPOSED

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Screen width/height
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640

# Initialize pygame
pygame.init

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Parent class for all bocks
class Block(pygame.sprite.Sprite):
    def __init__(self, set_x, set_y, set_type, set_is_you, set_can_push, set_is_win, set_is_stop, set_image):
        super(Block, self).__init__()
        # Dimensions in pixels
        self.dimension = (64, 64)
        self.x = set_x
        self.y = set_y
        self.type = set_type
        self.is_you = set_is_you
        self.can_push = set_can_push
        self.is_win = set_is_win
        self.is_stop = set_is_stop
        self.surf = pygame.image.load(set_image).convert_alpha()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    # Move function
    def move(block_to_move, pressed_keys):
        if True:
        # Move blocks based on key presses
            if pressed_keys[K_UP]:
                block_to_move.rect.move_ip(0, -64)
                cookie.y -= 64
            if pressed_keys[K_DOWN]:
                block_to_move.rect.move_ip(0, 64)
                cookie.y += 64
            if pressed_keys[K_LEFT]:
                block_to_move.rect.move_ip(-64, 0)
                cookie.x -= 64
            if pressed_keys[K_RIGHT]:
                block_to_move.rect.move_ip(64, 0)
                cookie.x += 64
    def move_adjacent(block_to_move, pressed_keys):
        if block_to_move.can_push:
        # Move blocks based on key presses
            if pressed_keys[K_UP]:
                block_to_move.rect.move_ip(0, -64)
                block_to_move.y -= 64
                return True
            if pressed_keys[K_DOWN]:
                block_to_move.rect.move_ip(0, 64)
                block_to_move.y += 64
                return True
            if pressed_keys[K_LEFT]:
                block_to_move.rect.move_ip(-64, 0)
                block_to_move.x -= 64
                return True
            if pressed_keys[K_RIGHT]:
                block_to_move.rect.move_ip(64, 0)
                block_to_move.x += 64
                return True
            return False
    

        # Keep blocks on screen
            if block_to_move.rect.left < 0:
                block_to_move.rect.left = 0
            if block_to_move.rect.right > SCREEN_WIDTH:
                block_to_move.rect.right = SCREEN_WIDTH
            if block_to_move.rect.top <= 0:
                block_to_move.rect.top = 0
            if block_to_move.rect.bottom >= SCREEN_HEIGHT:
                block_to_move.rect.bottom = SCREEN_HEIGHT
    def correct(pressed_keys):
      if pressed_keys[K_UP]:
          cookie.rect.move_ip(0, 64)
          cookie.y += 64
          return True
      if pressed_keys[K_DOWN]:
          cookie.rect.move_ip(0, -64)
          cookie.y -= 64
          return True
      if pressed_keys[K_LEFT]:
          cookie.rect.move_ip(64, 0)
          cookie.x += 64
          return True
      if pressed_keys[K_RIGHT]:
          cookie.rect.move_ip(-64, 0)
          cookie.x -= 64
          return True
      return True

# Object block class
class Object(Block):
    def __init__(self, set_x, set_y, set_is_you, set_can_push, set_is_win, set_is_stop, set_image):
        super().__init__(set_x, set_y, "Object", set_is_you, set_can_push, set_is_win, set_is_stop, set_image)


# Variable block class
class Variable(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Variable", False, True, False, True, set_image)

# Attribute block class
class Attribute(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Attribute", False, True, False, True, set_image)

# Operator block class
class Operator(Block):
    def __init__(self, set_x, set_y, set_image):
        super().__init__(set_x, set_y, "Operator", False, True, False, True, set_image)


# Create list of Objects for game
list_of_blocks = []

# Create instances and add them to the Block list

# Create all the Object instances, make a list of Objects, add that list to the Block list
# 0 is a placeholder until I figure out the correct positions
wafer_1 = Object(256, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_2 = Object(320, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_3 = Object(384, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_4 = Object(448, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_5 = Object(512, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_6 = Object(576, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_7 = Object(640, 160, False, False, False, True, "Project/Graphics/wafer.png")
wafer_8 = Object(256, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_9 = Object(320, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_10 = Object(384, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_11 = Object(448, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_12 = Object(512, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_13 = Object(576, 416, False, False, False, True, "Project/Graphics/wafer.png")
wafer_14 = Object(640, 416, False, False, False, True, "Project/Graphics/wafer.png")
milk = Object(640, 288, False, False, True, True, "Project/Graphics/milk.png")
donut_1 = Object(448, 224, False, True, False, True, "Project/Graphics/donut.png")
donut_2 = Object(448, 288, False, True, False, True, "Project/Graphics/donut.png")
donut_3 = Object(448, 352, False, True, False, True, "Project/Graphics/donut.png")
cookie = Object(256, 288, True, False, False, False, "Project/Graphics/cookie.png")
wafers = [wafer_1, wafer_2, wafer_3, wafer_4, wafer_5, wafer_6, wafer_7, wafer_8, wafer_9, wafer_10, wafer_11, wafer_12, wafer_13, wafer_14]
donuts = [donut_1, donut_2, donut_3]
cookiel = [cookie]
milkl = [milk]
list_of_objects = [cookiel, wafers, milkl, donuts]

# Create all of the Variable instances, make a Variable list, add that list to Block list
# 0 is a placeholder until I figure out the correct positions
cookie_word = Variable(64, 64, "Project/Graphics/cookieword.png")
wafer_word = Variable(748, 540, "Project/Graphics/waferword.png")
milk_word = Variable(64, 540, "Project/Graphics/milkword.png")
donut_word = Variable(748, 64, "Project/Graphics/donutword.png")
list_of_variables = [cookie_word, wafer_word, milk_word, donut_word]
list_of_blocks.append(list_of_variables)

# Create all of the Attribute instances, make an Attribute list, add that list to Block list
# 0 is a placeholder until I figure out the correct positions
you = Attribute(196, 64, "Project/Graphics/youword.png")
win = Attribute(196, 540, "Project/Graphics/winword.png")
stop = Attribute(876, 540, "Project/Graphics/stopword.png")
push = Attribute(876, 64, "Project/Graphics/pushword.png")
list_of_attributes = [you, win, stop, push]
list_of_blocks.append(list_of_attributes)

# Create the Operator instances, make Operator list, and add it to the list of blocks
is_1 = Operator(128, 64, "Project/Graphics/isword.png")
is_2 = Operator(812, 64, "Project/Graphics/isword.png")
is_3 = Operator(128, 540, "Project/Graphics/isword.png")
is_4 = Operator(812, 540, "Project/Graphics/isword.png")
list_of_operators = [is_1, is_2, is_3, is_4]
list_of_blocks.append(list_of_operators)

# Variable to keep the main loop running
running = True
canMoveCurrently = cookie # lol word is moving but not cookie
# Setup the clock for a decent framerate
clock = pygame.time.Clock()

while running:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():

        # Did the user hit a key?

        if event.type == KEYDOWN:

            # Was it the Escape key? If so, stop the loop.

            if event.key == K_ESCAPE:

                running = False


        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:

            running = False
        
        if(len(pressed_keys) != 0):
          Block.move(cookie, pressed_keys)
          for i in range(len(list_of_objects)):
            for block in list_of_objects[i]:
              if (abs(cookie.x - block.x) < 10 and abs(cookie.y - block.y) < 10 and cookie != block and not Block.move_adjacent(block, pressed_keys)):
                if (not block.is_win == True):
                  Block.correct(pressed_keys)
                else:
                  print('You Win!')
                  running = False

          for i in range(len(list_of_objects)):
            for block in list_of_objects[i]:
              if (abs(cookie.x - block.x) < 10 and abs(cookie.y - block.y) < 10 and cookie != block):
                Block.move_adjacent(block, pressed_keys)


    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    for entity in list_of_attributes:
        screen.blit(entity.surf, entity.rect)

    for entity in list_of_objects:
        if type(entity) == list:
            for block in entity:
                screen.blit(block.surf, block.rect)
        else:
            screen.blit(entity.surf, entity.rect)

    for entity in list_of_operators:
        screen.blit(entity.surf, entity.rect)

    for entity in list_of_variables:
        screen.blit(entity.surf, entity.rect)

    for entity in list_of_blocks:
        if type(entity) == list:
            for blok in entity:
                if type(blok) == list:
                    for blok2 in blok:
                        screen.blit(blok2.surf, blok2.rect)
                    else:
                        screen.blit(blok.surf, blok.rect)
        else:
            screen.blit(entity.surf, entity.rect)

    
    # Update the display
    pygame.display.flip()
