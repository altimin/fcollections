from __future__ import division

from collections import Counter
from collections import defaultdict

NO_ARGUMENT_PASSED = object()

import fcollections

class Iterable(object):
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return iter(self._iterable)

    def count(self, *args):
        if len(args) > 1:
            raise TypeError('count() takes at most 1 argument (%d given)' % len(args))
        if len(args) == 1:
            return self.filter(lambda value: value == args[0]).len()
        else:
            return Counter(self)

    def sort(self, key=None, reverse=False):
        return self.list().sort(key=key, reverse=reverse)

    def filter(self, predicate=None):
        if predicate is None:
            predicate = lambda item: item
        return Iterable(item for item in self if predicate(item))

    def map(self, func):
        return Iterable(func(item) for item in self)

    def starmap(self, func):
        return Iterable(func(*item) for item in self)

    def doublestarmap(self, func):
        return Iterable(func(**item) for item in self)

    def reduce(self, func, initial=NO_ARGUMENT_PASSED):
        iterator = iter(self)
        if initial is not NO_ARGUMENT_PASSED:
            value = initial
        else:
            try:
                value = next(iterator)
            except StopIteration:
                raise TypeError('reduce() of empty sequence with no initial value')
        for item in iterator:
            value = func(value, item)
        return value

    def list(self):
        return fcollections.List(self)

    def groupby(self, key):
        result = defaultdict(fcollections.List)
        for item in self:
            result[key(item)].append(item)
        return dict(result)

    def len(self):
        try:
            return len(self._iterable)
        except:
            return sum(1 for item in self)

    def max(self, key=None):
        if key is None:
            return max(self)
        else:
            return max(self, key=key)

    def min(self, key=None):
        if key is None:
            return min(self)
        else:
            return min(self, key=key)

    def any(self):
        return any(self)

    def all(self):
        return all(self)

    def sum(self):
        return sum(self)

    def take(self, count):
        return Iterable(item for i, item in enumerate(self) if i < count)

    def drop(self, count):
        return Iterable(item for i, item in enumerate(self) if i >= count)

    def takewhile(self, predicate):
        def helper():
            for item in self:
                if not predicate(item):
                    return
                yield item
        return Iterable(helper())

    def takeuntil(self, predicate):
        return self.takewhile(lambda x: not predicate(x))

    def dropwhile(self, predicate):
        def helper():
            iterator = iter(self)
            for item in iterator:
                if not predicate(item):
                    yield item
                    break
            for item in iterator:
                yield item
        return Iterable(helper())

    def dropuntil(self, predicate):
        return self.dropwhile(lambda x: not predicate(x))

    def unique(self):
        def helper(sequence):
            seen = set()
            for item in sequence:
                if item not in seen:
                    yield item
                    seen.add(item)
        return Iterable(helper(self))
