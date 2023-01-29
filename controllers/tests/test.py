import unittest
from models.book_class import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.title = 'Title'
        self.description = 'Description'
        self.author = 'Test'
        self.genre = 'test'
        self.checked_out = False

    def test_checkTitle(self):
        self.assertEqual ('Title', self.title)
        
    def test_checkDesc(self):
        self.assertEqual ('Description', self.description)
        

    def test_checkAuthor(self):
        self.assertEqual ('Test', self.author)
        
    def test_checkGenre(self):
        self.assertEqual ('test', self.genre)
        
    def test_checkCheckOut(self):
        self.assertEqual (False, self.checked_out)
        

    