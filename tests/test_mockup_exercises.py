# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch, MagicMock

from src.mockup_exercises import fetch_data_from_api, read_data_from_file, execute_command, perform_action_based_on_time


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("src.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """ Success case."""
        # Arrage
        url = "https://example.com/api/data"
        mock_get.return_value.json.return_value = {"key": "value"}
        mock_get.return_value.status_code = 200

        # Act
        data = fetch_data_from_api(url)

        # Assert
        self.assertEqual(data, {"key": "value"})

    @patch("src.mockup_exercises.open")
    def test_read_data_from_file_try(self, mock_open):
        """ Test read_data_from_file with try."""
        # Arrage
        filename = "test.txt"
        mock_open.return_value.__enter__.return_value.read.return_value = "data"

        # Act
        data = read_data_from_file(filename)

        # Assert
        self.assertEqual(data, "data")
        mock_open.assert_called_once_with(filename, encoding="utf-8")
        mock_open.return_value.__enter__.return_value.read.assert_called_once()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_from_file_not_found_error(self, mock_open):
        """Test read_data_from_file raises FileNotFoundError when file is missing."""
        # Arrange
        filename = "non_existing_file.txt"

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)

    @patch("src.mockup_exercises.subprocess.run")
    def test_execute_command_correct(self, mock_command):
        """Test execute_command function. correct """
        # Arrage
        command = "ls -l"
        mock_command.return_value.stdout = "mocked output"

        # Act
        result = execute_command(command)

        # Assert
        self.assertEqual(result, "mocked output")
        mock_command.assert_called_once_with(command, capture_output=True, check=False, text=True)

    @patch("src.mockup_exercises.subprocess.run")
    def test_execute_command_exception(self, mock_run):
        """Test execute_command returns stdout even when command fails (check=False)."""
        # Arrange
        command = ["invalid", "command"]
        mock_result = MagicMock()
        mock_result.returncode = 1  # simulate error,but launch exception why check=False
        mock_result.stdout = "Simulated stdout"
        mock_result.stderr = "Simulated error"
        mock_run.return_value = mock_result

        # Act
        result = execute_command(command)

        # Assert
        self.assertEqual(result, "Simulated stdout")

    @patch("src.mockup_exercises.time.time")
    def test_perform_action_based_on_time_A(self, mock_time):
        """ Test perform_action_based_on_time function."""
        #Arrage
        mock_time.return_value = 5

        #Act
        result = perform_action_based_on_time()

        #Assert
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()


    @patch("src.mockup_exercises.time.time")
    def test_perform_action_based_on_time_B(self, mock_time):
        """ Test perform_action_based_on_time function."""
        #Arrage
        mock_time.return_value = 12

        #Act
        result = perform_action_based_on_time()

        #Assert
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()