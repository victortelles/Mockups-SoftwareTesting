import unittest

from src.book_store import display, add_book, display_books, search_book


class TestBookStore(unittest.TestCase):
    """Unit test Book Store """

    def testBookOption1():
        """Test display function"""
