class GameStats():
    """Track statistics for game"""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def update_score(self, aliens_hit):
        """Updates score based on the number of aliens hit"""
        points_scored = aliens_hit * self.settings.alien_points
        self.score += points_scored
