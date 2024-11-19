import pygame

from constants import RED, TILE_SIZE



class Sprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

    def update(*args, **kwargs):
        ...

class Player(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()

        
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    

