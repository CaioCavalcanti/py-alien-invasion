import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overral class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.get_screen_size())
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_fleet()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Starts a new game when the player clicks play"""
        game_active = self.stats.game_active
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if not game_active and button_clicked:
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        self.scoreboard.render_score()
        self.scoreboard.render_level()
        self.settings.initialize_dynamic_settings()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center()
        pygame.mouse.set_visible(False)

    def _update_bullets(self):
        """Update bullets on the screen"""
        self.bullets.update()
        self._remove_bullets_off_screen()
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Check for bullets that hit aliens"""
        aliens_hit = self._count_aliens_hit_by_bullets()
        if aliens_hit > 0:
            self.stats.update_score(aliens_hit)
            self.scoreboard.render_score()
            self.scoreboard.check_highscore()
        if not self.aliens:
            self._start_new_level()

    def _count_aliens_hit_by_bullets(self):
        aliens_hit = 0
        # collisions is a dict where the key is the bullet
        # and the value is a list of aliens hit by that bullet
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                aliens_hit += len(aliens)
        return aliens_hit

    def _start_new_level(self):
        # Destroy existing bullets
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        self.stats.level += 1
        self.scoreboard.render_level()

    def _remove_bullets_off_screen(self):
        """Removes bullets that have disappeared from the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_fleet(self):
        """Update the position of the aliens"""
        self._check_fleet_reached_edge()
        self.aliens.update()
        self._check_ship_alien_collision()
        self._check_aliens_hit_bottom()

    def _check_fleet_reached_edge(self):
        """Checks if an alien reached an edge"""
        for alien in self.aliens.sprites():
            if alien.has_reached_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.drop()
        self.settings.fleet_direction *= -1

    def _check_ship_alien_collision(self):
        """Checks if ship was hit by any alien"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._hit_ship()

    def _hit_ship(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Get rid of any remaining aliens and bullets
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_hit_bottom(self):
        """Checks if any alien hit the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._hit_ship()
                break

    def _update_screen(self):
        """Redraw the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)
        self.scoreboard.draw()

        if not self.stats.game_active:
            self.play_button.draw()

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
        elif key_pressed == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()
        elif key_pressed == pygame.K_q:
            self._quit_game()
        elif key_pressed == pygame.K_SPACE:
            if self.stats.game_active:
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
