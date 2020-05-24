class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # indicates the fleet moving direction: 1 for right, -1 for left
        self.fleet_direction = 1

    def get_screen_size(self):
        """Returns a tuple with screen width and height"""
        return (self.screen_width, self.screen_height)

    def get_bullet_size(self):
        """Returns a tuple with bullet width and height"""
        return (self.bullet_width, self.bullet_height)
