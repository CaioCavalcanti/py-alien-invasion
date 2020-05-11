import sys
import unittest

sys.path.insert(1, '../alien_invasion')
from alien_invasion.settings import Settings

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


if __name__ == '__main__':
    unittest.main()
