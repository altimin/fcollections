import fcollections

import six

if six.PY2:
    keys = dict.iterkeys
    values = dict.itervalues
    items = dict.iteritems
else:
    keys = dict.keys
    values = dict.values
    items = dict.items

class Dict(dict):
    def keys(self):
        return fcollections.Iterable(keys(self))

    def values(self):
        return fcollections.Iterable(values(self))

    def items(self):
        return fcollections.Iterable(items(self))

    # python2 compatibility
    iterkeys = viewkeys = keys
    itervalues = viewvalues = values
    iteritems = viewitems = items

    def filter(self, predicate):
        return Dict((key, value) for (key, value) in self.items() if predicate(key, value))

    def filter_keys(self, predicate):
        return Dict((key, value) for (key, value) in self.items() if predicate(key))

    def filter_values(self, predicate):
        return Dict((key, value) for (key, value) in self.items() if predicate(value))

    def map(self, func):
        return Dict(func(key, value) for (key, value) in self.items())

    def map_keys(self, func):
        return Dict((func(key), value) for (key, value) in self.items())

    def map_values(self, func):
        return Dict((key, func(value)) for (key, value) in self.items())

    def len(self):
        return len(self)

    def copy(self):
        return Dict(self)

    def update(self, __iterable=None, **kwargs):
        if __iterable is not None:
            dict.update(self, __iterable, **kwargs)
        else:
            dict.update(self, **kwargs)
        return self

    def discard(self, key):
        return self.filter_keys(lambda k: k != key)

    def discard_keys(self, keys):
        keys = set(keys)
        return self.filter_keys(lambda key: key not in keys)

    def reduce_each(self, func, initial=fcollections.utils.NO_ARGUMENT_PASSED):
        return self.map_values(lambda value: fcollections.Iterable(value).reduce(func=func, initial=initial))

    def min_each(self, key=None):
        return self.map_values(lambda value: fcollections.Iterable(value).min(key=key))

    def max_each(self, key=None):
        return self.map_values(lambda value: fcollections.Iterable(value).max(key=key))

    def sum_each(self, start=0):
        return self.map_values(lambda value: fcollections.Iterable(value).sum(start=start))

    def len_each(self):
        return self.map_values(len)

    def average_each(self, default=fcollections.utils.NO_ARGUMENT_PASSED):
        return self.map_values(lambda value: fcollections.functions.average(value, default=default))

    def any_each(self):
        return self.map_values(lambda value: Iterable(value).any())

    def all_each(self):
        return self.map_values(lambda value: Iterable(value).all())

    def none_each(self):
        return self.map_values(lambda value: Iterable(value).none())
