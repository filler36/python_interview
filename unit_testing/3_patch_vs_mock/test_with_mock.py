import unittest
import main
from unittest.mock import Mock
from unittest.mock import patch


class GetUserInfoTest(unittest.TestCase):

    def test_get_user_info_with_mock(self):
        main.external_service = Mock(return_value={'name': 'Test User', 'age': 30})

        # Call the function that uses the mocked function
        result = main.get_user_info(user_id=3)

        # Assert that the result is as expected
        self.assertEqual(result, {'name': 'Test User', 'age': 30})

    def test_get_user_info_without_mock(self):
        # Call the function that uses external service without mocks
        result = main.get_user_info(user_id=3)

        # Assert that the result is as expected
        # This call will raise Exception because main.external_service was mocked in the previous test using Mock
        self.assertEqual(result, {'name': 'Filip', 'age': 35})

if __name__ == '__main__':
    unittest.main()
