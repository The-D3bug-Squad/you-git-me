import unittest
from unittest.mock import patch
import os

# Assuming your functions are defined in a file named `user_functions.py`
from Tools.helper_functions import get_password, get_username, validate_password, validate_username, save_user_info

class TestUserFunctions(unittest.TestCase):

    @patch("Tools.helper_functions.pwinput.pwinput", return_value="securePassword123!")
    def test_get_password(self, mock_input):
        result = get_password("Enter your password: ")
        self.assertEqual(result, "securePassword123!")

    @patch("builtins.input", return_value="user123")
    def test_get_username(self, mock_input):
        result = get_username("Enter your username: ")
        self.assertEqual(result, "user123")

    def test_validate_password(self):
        self.assertTrue(validate_password("Password123!"))
        self.assertFalse(validate_password("short"))  # Too short
        self.assertFalse(validate_password("password123"))  # No uppercase
        self.assertFalse(validate_password("PASSWORD123"))  # No lowercase
        self.assertFalse(validate_password("Password!"))  # No digit
        self.assertFalse(validate_password("Password123"))  # No special character

    def test_validate_username(self):
        self.assertTrue(validate_username("user"))
        self.assertFalse(validate_username("us"))  # Too short
        self.assertFalse(validate_username("user!"))  # Contains non-alphanumeric characters

    def test_save_user_info(self):
        test_file = "test_user_data.csv"
        if os.path.exists(test_file):
            os.remove(test_file)

        def mock_save_user_info(username, password):
            save_user_info(username, password)

        with patch("Tools.helper_functions.open", unittest.mock.mock_open()) as mock_file:
            mock_save_user_info("user123", "Password123!")
            mock_file.assert_called_once_with("user_data.csv", "a")
            handle = mock_file()
            handle.write.assert_called_once_with("user123,Password123!\n")

if __name__ == "__main__":
    unittest.main()
