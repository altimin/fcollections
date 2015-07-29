import fcollections

class List(list, fcollections.Iterable):
    def count(self, *args):
        return fcollections.Iterable.count(self, *args)

    def sort(self, key=None, reverse=False):
        list.sort(self, key=key, reverse=reverse)
        return self

    def insert(self, index, value):
        list.insert(self, index, value)
        return self

    def extend(self, iterable):
        list.extend(self, iterable)
        return self

    def append(self, value):
        list.append(self, value)
        return self

    def reverse(self):
        list.reverse(self)
        return self

    def __add__(self, other):
        return List(list.__add__(self, other))

    def __radd__(self, other):
        return List(list.__add__(other, self))

    def __mul__(self, other):
        return List(list.__mul__(self, other))

    def __rmul__(self, other):
        return List(list.__rmul__(self, other))
