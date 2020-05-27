class GameStats():
    """Track statistics for game"""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.highscore = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_score(self, aliens_hit):
        """Updates score based on the number of aliens hit"""
        points_scored = aliens_hit * self.settings.alien_points
        rounded_points_scored = round(points_scored, -1)
        self.score += rounded_points_scored

    def has_new_highscore(self):
        if self.score > self.highscore:
            self._update_highscore()
            return True
        else:
            return False

    def _update_highscore(self):
        self.highscore = self.score
