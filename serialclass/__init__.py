""" Library that adds a base class to be used to get a serialized representation of Python classes and their attributes.

Copyright (c) 2020 Greg Van Aken
"""
BUILDNUM = 'dev'  # on CI builds - this is replaced with auto-incrementing build num
__version__ = f'0.0.1.{BUILDNUM}'

from serialclass.serialclass import SerialClass
