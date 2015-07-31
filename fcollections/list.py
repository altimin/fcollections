import fcollections

class List(list, fcollections.Iterable):
    def count(self, *args):
        return fcollections.Iterable.count(self, *args)

    def insert(self, index, value):
        list.insert(self, index, value)
        return self

    def extend(self, iterable):
        list.extend(self, iterable)
        return self

    def append(self, value):
        list.append(self, value)
        return self

    def copy(self):
        return List(self)

    def sort(self, key=None, reverse=False):
        list.sort(self, key=key, reverse=reverse)
        return self

    def sorted(self, key=None, reverse=False):
        return List(sorted(self, key=key, reverse=reverse))

    def reverse(self):
        list.reverse(self)
        return self

    def reversed(self):
        return fcollections.Iterable(reversed(self))

    def __add__(self, other):
        return List(list.__add__(self, other))

    def __radd__(self, other):
        return List(list.__add__(other, self))

    def __mul__(self, other):
        return List(list.__mul__(self, other))

    def __rmul__(self, other):
        return List(list.__rmul__(self, other))

    def __getslice__(self, *args):
        return List(list.__getslice__(self, *args))

    def __setslice__(self, *args):
        return List(list.__setslice__(self, *args))

    def __getitem__(self, index):
        if isinstance(index, slice):
            return List(list.__getitem__(self, index))
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            return List(list.__setitem__(self, index, value))
        return list.__setitem__(self, index, value)
