class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_spped = 1.5

    def get_screen_size(self):
        """Returns a tuple with screen width and height"""
        return (self.screen_width, self.screen_height)
