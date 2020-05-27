import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare the initial images
        self.render_score()
        self.render_highscore()
        self.render_level()
        self.render_ships()

    def render_score(self):
        """Render the score as an image"""
        score = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            score, True, self.text_color, self.settings.bg_color)
        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def render_highscore(self):
        """Render the highscore as an image"""
        highscore = "{:,}".format(self.stats.highscore)
        self.highscore_image = self.font.render(
            highscore, True, self.text_color, self.settings.bg_color)
        # display the highscore at the top center of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top

    def render_level(self):
        """Render the current level as an image"""
        level = str(self.stats.level)
        self.level_image = self.font.render(
            level, True, self.text_color, self.settings.bg_color)
        # display the current level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def render_ships(self):
        """Shows how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def draw(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_highscore(self):
        if self.stats.has_new_highscore():
            self.render_highscore()
