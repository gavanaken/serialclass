"""Set of unittests for serialclass module

Copyright (c) 2020 Greg Van Aken
"""

import unittest
import json
from test_helpers import Expected, Library


class TestArbitraryClasses(unittest.TestCase):
    """A bunch of classes being serialized"""

    def test_book(self):
        """Serialize a book object!"""
        book = Library.Book()
        self.assertEqual({'Book': {'physical': True, 'useful': True}}, book.serialize())

    def test_hp(self):
        """Serailize Harry Potter"""
        hp = Library.HarryPotter()
        expected = Expected.test_hp
        self.assertEqual(expected, hp.serialize())
        self.assertEqual(json.dumps(expected), hp.stringify())

    def test_vhc(self):
        """Serialize Hungry Caterpillar"""
        hc = Library.HungryCaterpillar()
        expected = Expected.test_vhc
        self.assertEqual(expected, hc.serialize())
        self.assertEqual(json.dumps(expected), hc.stringify())

    def test_bookshelf(self):
        """Testing a bookshelf of shelves of books"""
        hc = Library.HungryCaterpillar()
        hp = Library.HarryPotter()
        bookshelf = Library.Bookshelf(4)
        bookshelf.stock_shelf(2, [hc, hp])
        expected = Expected.test_bookshelf
        self.assertEqual(expected, bookshelf.serialize())
