LIGHT_GRAY=(230,230,230)
DARK_GRAY=(60,60,60)

class Settings:
    """
    A class to control the game settings
    
    Attributes:
        screen_width (int) the screen width
        screen_height (int) the screen height
        bg_color (tuple of int) the background color of the screen
        ship_limit (int) max number of ships a player have when a new game starts
        bullet_width (int) the bullet width
        bullet_height (int) the bullet height
        bullet_color (tuple of int) the color of the bullet
        bullets_allowed (int) max number of bullets a player can fire simultaneously
            on the screen
        fleet_drop_speed (int) the number of pixels the aliens will drop on the 
            screen after reaching the edge
        speedup_scale (float) how fast the game tempo should increase on each
            new phase
        score_scale (float) how the points for hitting a alien should increase
            on each new phase
        alien_points (int) how many points the player scores for hitting an alien
        ship_speed (float) how fast the ship moves on the screen
        bullet_speed (float) how fast the bullet moves on the screen
        alien_speed (float) how fast the aliens move on the screen
        fleet_direction (int) the direction the alien fleet is moving on the screen,
            1 for right and -1 for left
    """

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = LIGHT_GRAY
        # Ship settings
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = DARK_GRAY
        self.bullets_allowed = 3
        # Alien settings
        self.fleet_drop_speed = 10
        # how quickly the game speeds up
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game with default values
        
        Args:
            None

        Returns:
            None
        """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # indicates the fleet moving direction: 1 for right, -1 for left, we use
        # these values to make it easier to move the aliens on the screen, by
        # just adding the diretion to the alien.rect.width
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """
        Increase game tempo and alien points
        
        Args:
            None

        Returns:
            None
        """
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def get_screen_size(self):
        """
        Gets the screen size

        Args:
            None

        Returns:
            tuple of ints (width, height): the screen size
        """
        return (self.screen_width, self.screen_height)

    def get_bullet_size(self):
        """
        Gets the bullet size

        Args:
            None

        Returns:
            tuple of ints (width, height): the bullet size
        """
        return (self.bullet_width, self.bullet_height)
