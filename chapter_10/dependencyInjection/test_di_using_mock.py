import unittest
from using_mock import WeatherService

class MockWeatherApiClient:
    def fetch_weather(self, location):
        return f"Mock weather data for {location}"
    

class TestWeatherService(unittest.TestCase):
    def test_get_weather(self):
        mock_api = MockWeatherApiClient()
        weather_service = WeatherService(mock_api)
        self.assertEqual(
            weather_service.get_weather("Anywhere"),
            "Mock weather data for Anywhere"
        )

if __name__ == "__main__":
    unittest.main()