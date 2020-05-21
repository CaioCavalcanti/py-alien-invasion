from pygame.sprite import Sprite
from helpers import load_image


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = load_image('alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def drop(self):
        """Move the alien down the screen"""
        self.rect.y += self.settings.fleet_drop_speed

    def has_reached_edge(self):
        """Checks if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        reached_right = self.rect.right >= screen_rect.right
        reached_left = self.rect.left <= 0
        if reached_right or reached_left:
            return True
