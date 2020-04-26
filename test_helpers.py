"""Set of helpers for serialclass module

Copyright (c) 2020 Greg Van Aken
"""

from serialclass import SerialClass


class Expected:
    """Some expected responses from our tests"""
    test_bookshelf = {
        "Bookshelf": {
            "color": "dark brown",
            "material": "wood",
            "shelves": [
                {
                    "Shelf": {
                        "books": [],
                        "capacity": 10
                    }
                },
                {
                    "Shelf": {
                        "books": [],
                        "capacity": 10
                    }
                },
                {
                    "Shelf": {
                        "books": [
                            {
                                "HungryCaterpillar": {
                                    "author": "Eric Carle",
                                    "chapters": 0,
                                    "pages": 32,
                                    "physical": True,
                                    "title": "The Very Hungry Caterpillar",
                                    "useful": True,
                                    "words": 224
                                }
                            },
                            {
                                "HarryPotter": {
                                    "author": "J.K Rowling",
                                    "chapters": 17,
                                    "pages": 223,
                                    "physical": True,
                                    "pictures": 0,
                                    "title": "Harry Potter and the Philosopher's Stone",
                                    "useful": True,
                                    "words": 76944
                                }
                            }
                        ],
                        "capacity": 10
                    }
                },
                {
                    "Shelf": {
                        "books": [],
                        "capacity": 10
                    }
                }
            ]
        }
    }

    test_hp = {
        'HarryPotter':
            {
                'author': 'J.K Rowling',
                'chapters': 17,
                'pages': 223,
                'physical': True,
                'pictures': 0,
                'title': "Harry Potter and the Philosopher's Stone",
                'useful': True,
                'words': 76944
            }
    }

    test_vhc = {
        'HungryCaterpillar':
            {
                'author': 'Eric Carle',
                'chapters': 0,
                'pages': 32,
                'physical': True,
                'title': 'The Very Hungry Caterpillar',
                'useful': True,
                'words': 224
            }
    }

    test_bookshelf_depth_1 = {
        "Bookshelf": {
            "color": "dark brown",
            "material": "wood",
            "shelves": [
                "<test_helpers.Library.Shelf object>",
                "<test_helpers.Library.Shelf object>",
                "<test_helpers.Library.Shelf object>",
                "<test_helpers.Library.Shelf object>"
            ]
        }
    }

    test_ignore_protected = {'Diary': {'_secret': 'My dirty little secret', 'joke': 'Knock, knock!'}}

    test_ignore_protected_true = {'Diary': {'joke': 'Knock, knock!'}}


class Library:
    """A class to hold some library-themed test classes"""

    class Book(SerialClass):
        """Just a book"""

        def __init__(self):
            self.physical = True
            self.useful = True

    class ChapterBook(Book):
        """A chapter book"""

        def __init__(self):
            super().__init__()
            self.pictures = 0

    class PictureBook(Book):
        """A picture book"""

        def __init__(self):
            super().__init__()
            self.chapters = 0

    class HarryPotter(ChapterBook):
        """An example chapter book"""

        def __init__(self):
            super().__init__()
            self.title = "Harry Potter and the Philosopher's Stone"
            self.author = "J.K Rowling"
            self.chapters = 17
            self.words = 76944
            self.pages = 223

    class HungryCaterpillar(PictureBook):
        """An example picture book"""

        def __init__(self):
            super().__init__()
            self.title = "The Very Hungry Caterpillar"
            self.author = "Eric Carle"
            self.words = 224
            self.pages = 32

    class Shelf(SerialClass):
        """A single shelf that holds books"""

        def __init__(self):
            self.capacity = 10
            self.books = []

    class Bookshelf(SerialClass):
        """A collection of books"""

        def __init__(self, num_shelves):
            self.shelves = [Library.Shelf() for _ in range(num_shelves)]
            self.material = 'wood'
            self.color = 'dark brown'

        def stock_shelf(self, i, books):
            """Add a set of books to shelf i"""
            shelf_i = self.shelves[i]
            if len(books) < (shelf_i.capacity - len(shelf_i.books)):
                shelf_i.books += books


class Diary(SerialClass):
    """A diary of secrets"""

    def __init__(self):
        self._secret = "My dirty little secret"
        self.joke = "Knock, knock!"
