

from helpers import load_image


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = load_image('ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement control
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on current moving direction"""
        ship_speed = self.settings.ship_speed
        if self.is_moving_right and self.rect.right < self.screen_rect.right:
            self.x += ship_speed
        if self.is_moving_left and self.rect.left > 0:
            self.x -= ship_speed
        if self.is_moving_up and self.rect.top > 0:
            self.y -= ship_speed
        if self.is_moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += ship_speed
        # Update rect object position
        self.rect.x = self.x
        self.rect.y = self.y

    def center(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
