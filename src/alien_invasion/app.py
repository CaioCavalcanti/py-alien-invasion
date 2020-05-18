import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overral class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.get_screen_size())
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_event(event.key)
            elif event.type == pygame.KEYUP:
                self._handle_keyup_event(event.key)

    def _update_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _handle_keydown_event(self, key_pressed):
        if key_pressed == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif key_pressed == pygame.K_LEFT:
            self.ship.is_moving_left = True
        elif key_pressed == pygame.K_q:
            self._quit_game()

    def _handle_keyup_event(self, key_pressed):
        if key_pressed == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif key_pressed == pygame.K_LEFT:
            self.ship.is_moving_left = False

    def _quit_game(self):
        sys.exit()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
