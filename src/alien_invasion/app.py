import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet


class AlienInvasion:
    """Overral class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.get_screen_size())
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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

    def _update_bullets(self):
        """Update bullets on the screen"""
        self.bullets.update()
        self._remove_bullets()

    def _remove_bullets(self):
        """Removes bullets that have disappeared from the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _handle_keydown_event(self, key_pressed):
        if key_pressed == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif key_pressed == pygame.K_LEFT:
            self.ship.is_moving_left = True
        elif key_pressed == pygame.K_UP:
            self.ship.is_moving_up = True
        elif key_pressed == pygame.K_DOWN:
            self.ship.is_moving_down = True
        elif key_pressed == pygame.K_q:
            self._quit_game()
        elif key_pressed == pygame.K_SPACE:
            self._fire_bullet()

    def _handle_keyup_event(self, key_pressed):
        if key_pressed == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif key_pressed == pygame.K_LEFT:
            self.ship.is_moving_left = False
        elif key_pressed == pygame.K_UP:
            self.ship.is_moving_up = False
        elif key_pressed == pygame.K_DOWN:
            self.ship.is_moving_down = False

    def _fire_bullet(self):
        """Creates a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        number_rows = self._get_number_rows(alien.rect.height)
        number_aliens = self._get_number_aliens_per_row(alien.rect.width)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens):
                self._create_alien(alien_number, row_number)

    def _get_number_aliens_per_row(self, alien_width):
        alien_required_width = 2 * alien_width
        available_width = self.settings.screen_width - alien_required_width
        number_aliens = available_width // alien_required_width
        return number_aliens

    def _get_number_rows(self, alien_height):
        available_height = (self.settings.screen_height -
                            (3 * alien_height) - self.ship.rect.height)
        number_rows = available_height // (2 * alien_height)
        return number_rows

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _quit_game(self):
        sys.exit()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
