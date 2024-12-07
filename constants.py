from typing import Literal
import pygame
WIDTH,HEIGHT = 800,800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60
# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK: tuple[Literal[0], Literal[0], Literal[0]] = (0, 0, 0)
BLUE: tuple[Literal[0], Literal[0], Literal[255]] = (0, 0, 255)
GREY: tuple[Literal[128], Literal[128], Literal[128]] = (128,128,128)

CROWN: pygame.Surface = pygame.transform.scale(pygame.image.load('crown.jpg'), (44, 25))





