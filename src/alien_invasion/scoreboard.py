import pygame.font


class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.render_score()

    def render_score(self):
        """Render the score as an image"""
        rounded_score = round(self.stats.score, -1)
        score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score, True, self.text_color, self.settings.bg_color)
        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)