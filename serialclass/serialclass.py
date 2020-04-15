""" BaseClass entry point - imported by __init__.py

Copyright (c) 2020 Greg Van Aken
"""

import re
import json


class SerialClass:
    """A base class that enables serialized representation of Python classes"""

    def class_attr(self, attr):
        """Make sure it is just an attribute and not a method, magic or otherwise"""
        return re.match('^(?!__).*', attr) and not callable(getattr(self, attr))

    def serialize(self, *args, **kwargs):
        """Get the serialized representation as a dict"""
        attribs = {}
        depth = kwargs.get('depth', float('inf'))
        calls = kwargs.get('calls', 0)
        for attr in dir(self):
            if self.class_attr(attr):
                attribs[attr] = self.unpack(getattr(self, attr), depth=depth, calls=calls)
        return {type(self).__name__: attribs}

    def stringify(self, *args, **kwargs):
        """Get a jsonstring from the dict representation of the class"""
        return json.dumps(self.serialize(*args, **kwargs), default=lambda o: str(o))

    def pstringify(self, *args, **kwargs):
        """Get a pretty jsonstring from the dict representation of the class"""
        return json.dumps(self.serialize(*args, **kwargs), indent=4, sort_keys=True, default=lambda o: str(o))

    def __iter__(self):
        """All the magic happens here"""
        for attr in dir(self):
            if self.class_attr(attr):
                yield attr, self.unpack(getattr(self, attr))

    # --Static Methods-- #
    @staticmethod
    def unpack(el, depth=float('inf'), calls=0):
        """Given an attribute value, make it a dict if possible"""
        if calls < depth:
            try:
                return el.serialize(depth=depth, calls=calls + 1)
            except (AttributeError):
                if isinstance(el, list):
                    return [SerialClass.unpack(item, depth=depth, calls=calls + 1) for item in el]
                elif isinstance(el, dict):
                    return {SerialClass.unpack(k, depth=depth, calls=calls + 1): el[k] for k in el}
        return el