import unittest
from unittest.mock import patch
from main import get_user_info, external_service


class GetUserInfoTest(unittest.TestCase):

    @patch('main.external_service')
    def test_get_user_info_with_patch(self, mock_external_service):
        # Set up the mock return value
        mock_external_service.return_value = {'name': 'Test User', 'age': 30}

        # Call the function that uses the mocked service
        result = get_user_info(user_id=3)

        # Assert that the result is as expected
        self.assertEqual(result, {'name': 'Test User', 'age': 30})


    def test_get_user_info_without_patch_and_mock(self):

        # Call the function that uses external service without mocks
        result = get_user_info(user_id=1)

        # Assert that the result is as expected
        # As you see, the external_service that was patched in the previous test is original again
        self.assertEqual(result, {'name': 'Filip', 'age': 35})


if __name__ == '__main__':
    unittest.main()
