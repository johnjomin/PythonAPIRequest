import unittest
from unittest.mock import patch
import GoldData

class TestGold(unittest.TestCase):

    def test_gold(self):
        # fakeNumber = 500

        with patch("GoldData.requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            # mock_get.return_value.json.return_value = fakeNumber

            obj = GoldData.Gold()
            response = obj.get

        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()