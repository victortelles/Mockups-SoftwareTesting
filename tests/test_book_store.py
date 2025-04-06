"""Unit tests for the BookStore system using mocks and assertions."""

# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, call, patch

# Import class main
from src.book_store import Book, BookStore


class TestBookStore(unittest.TestCase):
    """Unit test Book Store"""

    def setUp(self):
        """Set up for each test"""
        self.bookstore = BookStore()

    def test_book_display(self):
        """Test Book.Display methods outputs correct information"""
        # Arrage
        book = Book("Harry Potter", "J.K. Rowling", 10.99, 10)

        # Act & Assert
        with patch("builtins.print") as mock_print:
            book.display()

            # Check prints
            expected_calls = [
                unittest.mock.call("Title: Harry Potter"),
                unittest.mock.call("Author: J.K. Rowling"),
                unittest.mock.call("Price: $10.99"),
                unittest.mock.call("Quantity: 10"),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 4)

    def test_add_book(self):
        """Test BookStore.add_book method a book to the store"""
        # Arrage:
        mock_book = Mock()
        mock_book.title = "Mock Book"

        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.add_book(mock_book)

        # Assert
        self.assertIn(mock_book, self.bookstore.books)
        mock_print.assert_called_once_with("Book 'Mock Book' added to the store.")

    def test_display_books_empty(self):
        """Test BookStore.display_books method when store is empty"""
        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.display_books()

        # Assert
        mock_print.assert_called_once_with("No books in the store.")

    def test_display_books_with_books(self):
        """Test BookStore.display_books with books in the store"""
        # Arrage
        mock_book1 = Mock()
        mock_book2 = Mock()
        self.bookstore.books = [mock_book1, mock_book2]

        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.display_books()

        # Assert
        # Verify first print calls
        mock_print.assert_any_call("Books available in the store:")
        # verify that display() was called on each book
        mock_book1.display.assert_called_once()
        mock_book2.display.assert_called_once()

    def test_search_book_not_found(self):
        """Test bookStore.search_book when book is not found"""
        # Arrage
        mock_book = Mock()
        mock_book.title = "Existing Book"
        self.bookstore.books = [mock_book]

        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.search_book("Non Existent Book")

        # Assert
        mock_print.assert_called_once_with(
            "No book found with title 'Non Existent Book'."
        )

    def test_search_book_found(self):
        """Test BookStore.search_book when book is found"""
        # Arrage
        mock_book = Mock()
        mock_book.title = "Python Basics"
        self.bookstore.books = [mock_book]

        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.search_book("Python Basics")

        # Assert
        mock_print.assert_any_call("Found 1 book(s) with title 'Python Basics':")
        mock_book.display.assert_called_once()

    def test_search_book_case_insensitive(self):
        """Test BookStore.search_book is case insensitive"""
        # Arrage
        mock_book = Mock()
        mock_book.title = "Python Basics"
        self.bookstore.books = [mock_book]

        # Act
        with patch("builtins.print") as mock_print:
            self.bookstore.search_book("python basics")

        # Assert
        mock_print.assert_any_call("Found 1 book(s) with title 'python basics':")
        mock_book.display.assert_called_once()

    def test_main_function(self):
        """Test the main function with various inputs"""
        # create mock BookStore instance and methods
        mock_bookstore = Mock(spec=BookStore)

        # Mock the input functions to simulate user inputs
        inputs = iter(
            [
                "1",
                "2",
                "Python Book",
                "3",
                "Test Book",
                "Author",
                "10.99",
                "5",
                "4",
            ]
        )

        # Test the main function with mocked input/output and Bookstore
        with patch("builtins.input", side_effect=lambda _: next(inputs)), patch(
            "builtins.print"
        ), patch("src.book_store.BookStore", return_value=mock_bookstore), patch(
            "src.book_store.Book"
        ) as mock_book_class:

            # configure the mock Book class return a mock book
            mock_book = Mock()
            mock_book_class.return_value = mock_book

            # Import main after patching dependencies
            from src.book_store import main

            # Run the main function
            main()

            # Verify that the bookstore methods were called correctly
            mock_bookstore.display_books.assert_called_once()
            mock_bookstore.search_book.assert_called_once_with("Python Book")
            mock_bookstore.add_book.assert_called_once_with(mock_book)

            # Verify that Book constructor was called with correct parameters
            mock_book_class.assert_called_once_with("Test Book", "Author", 10.99, 5)
