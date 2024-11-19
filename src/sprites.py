import pygame

from constants import RED, TILE_SIZE


class Sprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

    def update(): ...


class Player(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 10

    def move(self):
        """
        Inspiration:
        https://stackoverflow.com/questions/16183265/how-to-move-sprite-in-pygame
        """
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:  # down key
            self.rect.y += self.speed  # move down
        elif key[pygame.K_w]:  # up key
            self.rect.y -= self.speed  # move up
        if key[pygame.K_d]:  # right key
            self.rect.x += self.speed  # move right
        elif key[pygame.K_a]:  # left key
            self.rect.x -= self.speed  # move left

    def update(self):
        self.move()
