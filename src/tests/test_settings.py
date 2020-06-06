import sys
import unittest

from alien_invasion.settings import Settings

sys.path.insert(1, '../alien_invasion')


class SettingsTests(unittest.TestCase):
    """Tests for the Settings class"""

    def setUp(self):
        """Create a Settings instance to be used in all test methods"""
        self.settings = Settings()

    def test_screen_size_is_1200x800(self):
        """Test that screen is set to 1200x800 by default"""
        assert self.settings.screen_width == 1200
        assert self.settings.screen_height == 800

    def test_background_color_is_grey(self):
        """Test that background color is set to grey by default"""
        assert self.settings.bg_color == (230, 230, 230)

    def test_get_screen_size_is_tuple(self):
        """Tests that screen size returns a tuple with screen width and height"""
        assert self.settings.get_screen_size() == (1200, 800)

    def test_ship_speed_is_1point5(self):
        """Tests that ship speed is set to 1.5 by default"""
        assert self.settings.ship_speed == 1.5

    def test_ship_limit_is_3(self):
        """Tests that the limit of ships is set to 3 by default"""
        assert self.settings.ship_limit == 3

    def test_bullet_speed_is_3(self):
        """Tests that bullet speed is set to 3 by default"""
        assert self.settings.bullet_speed == 3.0

    def test_bullet_size_is_3x15(self):
        """Tests that bullet size is set to 3x15 by default"""
        assert self.settings.bullet_width == 3
        assert self.settings.bullet_height == 15

    def test_bullet_color_is_dark_grey(self):
        """Tests that bullet color is set to dark grey by default"""
        assert self.settings.bullet_color == (60, 60, 60)

    def test_get_bullet_size_is_tuple(self):
        """Tests that get_bullet_size returns a tuple with bullet width and height"""
        assert self.settings.get_bullet_size() == (3, 15)

    def test_bullets_allowed_is_3(self):
        """Tests that only 3 bullets are allowed by default"""
        assert self.settings.bullets_allowed == 3

    def test_alien_speed(self):
        """Tests that alien default speed is 1"""
        assert self.settings.alien_speed == 1.0

    def test_fleet_drop_speed(self):
        """Tests that the alien fleet drop speed is 10 by default"""
        assert self.settings.fleet_drop_speed == 10

    def test_fleet_direction(self):
        """Tests that the alien fleet starts moving to the right by default"""
        assert self.settings.fleet_direction == 1


if __name__ == '__main__':
    unittest.main()
