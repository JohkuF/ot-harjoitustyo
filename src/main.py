import pygame

from constants import HEIGHT, WIDTH, TILE_SIZE
from graphics import draw_level, get_player_sprites
from sprites import Player
from world import world


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Platformer Game")
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        draw_level(self.screen, world)

        # Create sprite groups
        # NOTE: 
        self.players: pygame.sprite.Group = get_player_sprites(world)
        #self.all_sprites: pygame.sprite.Group = get_sprite_group(world)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill((0, 0, 0))

            self.players.update()
            self.players.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
