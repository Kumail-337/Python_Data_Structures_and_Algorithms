from typing import MutableMapping


class MapBaseClass(MutableMapping):
    class Item:
        __slots__ = 'key','value'

        def __init__(self,k,v):
            self.key = k
            self.value = v

        def eq (self, other):
            return self. key == other. key

        def ne (self, other):
            return not (self == other)

        def lt (self, other):
            return self. key < other. key

