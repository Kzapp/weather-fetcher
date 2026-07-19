import unittest
from weather_api import get_temperature

class TestWeather(unittest.TestCase):

    def test_valid_temperature(self):
        temp = get_temperature(26.64, -81.87)
        self.assertIsNotNone(temp)
        self.assertIsInstance(temp, float)

    def test_invalid_coordinates(self):
        temp = get_temperature(999, 999)
        self.assertIsNone(temp)

if __name__ == "__main__":
    unittest.main()