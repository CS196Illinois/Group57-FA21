# Import pygame
import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    # K_ESCAPE,
    # KEYDOWN,
    # QUIT,
)

# Screen width/height
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640

# Initialize pygame
pygame.init

# Parent class for all bocks
class Block(pygame.sprite.Sprite):
    def __init__(self, set_x, set_y, set_type, set_is_you, set_can_push, set_is_win, set_is_stop, set_image):
        super().__init__(Block, self)
        # Dimensions in pixels
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

    # Move function
    def move(self, pressed_keys):
        # Move blocks based on key presses
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep blocks on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


