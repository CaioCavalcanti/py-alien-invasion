class GameStats():
    """ Game stats class for tracking and managing score and game level.

    Attributes:
        score (int) the score of the current game
        level (int) the level of the current game
        ships_left (int) the number of ships left for the player on the current
            game
        game_active (bool) represents if the game is active
        highscore (int) the highest score achieved on all sessions played
    """

    def __init__(self, ai_game):
        """ Initializes game statistics

        Args:
            ai_game (AlienInvasion): current game instance
        """

        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.highscore = 0

    def reset_stats(self):
        """ Reset statistics that can change when a new game starts

        Args:
            None

        Returns:
            None
        """

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_score(self, aliens_hit):
        """ Updates score based on the number of aliens hit

        Args:
            aliens_hit (int) number of aliens hit by ship

        Returns:
            None
        """

        points_scored = aliens_hit * self.settings.alien_points
        rounded_points_scored = round(points_scored, -1)
        self.score += rounded_points_scored

    def has_new_highscore(self):
        """ Checks if current score is new highscore

        Args:
            None

        Returns:
            bool: whether the current score is new highscore
        """

        if self.score > self.highscore:
            self._update_highscore()
            return True
        else:
            return False

    def _update_highscore(self):
        """ Sets current score as highscore

        Args:
            None

        Returns:
            None
        """

        self.highscore = self.score
