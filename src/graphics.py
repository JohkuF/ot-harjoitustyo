import pygame

from constants import TILE_SIZE, WHITE
from sprites import Player

def draw_level(screen, level):
    for i, row in enumerate(level):
        for j, tile in enumerate(row):
            if tile == 1:  # GROUND
                pygame.draw.rect(
                    screen,
                    WHITE,
                    [j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE],
                )

def get_player_sprites(level) -> pygame.sprite.Group:
    player_sprites = pygame.sprite.Group()
    for i, row in enumerate(level):
        for j, sprite in enumerate(row):
            if sprite == 2: # DRAW PLAYER
                player_sprites.add(Player(j*TILE_SIZE, i*TILE_SIZE))
    return player_sprites

"""
def get_sprite_group(level) -> pygame.sprite.Group:
    all_sprites = pygame.sprite.Group()
    for i, row in enumerate(level):
        for j, sprite in enumerate(row):
            if sprite == 2: # DRAW PLAYER
                all_sprites.add(Player(j*TILE_SIZE, i*TILE_SIZE))
    return all_sprites
"""

