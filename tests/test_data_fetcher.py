# -*- coding: utf-8 -*-

"""
Mockup unit testing examples.
"""
import unittest
from unittest.mock import patch

from src.data_fetcher import fetch_data_from_api


class TestFecthDataFromApi(unittest.TestCase):
    """
    fetch_data_from_api unittest class.
    """

    def test_fetch_data_from_api(self):
        """
        Test the fetch_data_from_api function.
        """
        url = "https://jsonplaceholder.typicode.com/posts"

        # Mock the requests.get method
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = [
                {"id": 1, "title": "Title 1", "body": "Body 1"},
                {"id": 2, "title": "Title 2", "body": "Body 2"},
            ]

        # mock_get = patch('requests.get')
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = [
        #     {"id": 1, "title": "Title 1", "body": "Body 1"},
        #     {"id": 2, "title": "Title 2", "body": "Body 2"},
        # ]

        data = fetch_data_from_api(url)

        # Verify data is what we expect
        self.assertEqual(data[0]["id"], 1)


# class TestPrint(unittest.TestCase):
#     """
#     fetch_data_from_api unittest class.
#     """
#
#     def test_print(self):
#         # Mock the requests.get method
#         mock_print = patch('__main__.print')
#
#         print_hello_world()
#
#         # Verify data is what we expect
#         mock_print.assert_called_once_with("Hello, World!")
