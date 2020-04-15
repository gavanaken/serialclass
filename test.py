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
        self.assertEqual(Expected.test_hp, hp.serialize())
        self.assertEqual(json.dumps(Expected.test_hp), hp.stringify())

    def test_vhc(self):
        """Serialize Hungry Caterpillar"""
        hc = Library.HungryCaterpillar()
        self.assertEqual(Expected.test_vhc, hc.serialize())
        self.assertEqual(json.dumps(Expected.test_vhc), hc.stringify())

    def test_bookshelf(self):
        """Testing a bookshelf of shelves of books"""
        hc = Library.HungryCaterpillar()
        hp = Library.HarryPotter()
        bookshelf = Library.Bookshelf(4)
        bookshelf.stock_shelf(2, [hc, hp])
        self.assertEqual(Expected.test_bookshelf, bookshelf.serialize())

    def test_bookshelf_depth_1(self):
        """Testing that we can decrease our depth"""
        hc = Library.HungryCaterpillar()
        hp = Library.HarryPotter()
        bookshelf = Library.Bookshelf(4)
        bookshelf.stock_shelf(2, [hc, hp])
        self.assertEqual(json.dumps(Expected.test_bookshelf_depth_1), bookshelf.stringify(depth=1))
