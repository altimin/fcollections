import unittest

import fcollections
from fcollections import Dict

class DictTest(unittest.TestCase):
    def setUp(self):
        self.data = Dict({1: 'a', 2: 'b0', 3: 'C'})

    def checkAsSet(self, result, expected):
        self.assertTrue(isinstance(result, fcollections.Iterable))
        self.assertEqual(set(result), expected)

    def checkAsDict(self, result, expected):
        self.assertTrue(isinstance(result, fcollections.Dict))
        self.assertEqual(dict(result), expected)

    def test_basic_iteration(self):
        self.checkAsSet(self.data.keys(), {1, 2, 3})
        self.checkAsSet(self.data.values(), {'a', 'b0', 'C'})
        self.checkAsSet(self.data.items(), {(1, 'a'), (2, 'b0'), (3, 'C')})

    def test_filter(self):
        self.checkAsDict(self.data.filter(lambda key, value: key != 1 and value != 'C'), {2: 'b0'})
        self.checkAsDict(self.data.filter_keys(lambda key: key > 1), {2: 'b0', 3: 'C'})
        self.checkAsDict(self.data.filter_values(lambda value: value.isupper()), {3: 'C'})

    def test_map(self):
        self.checkAsDict(self.data.map(lambda key, value: (value, key)), {'a': 1, 'b0': 2, 'C': 3})
        self.checkAsDict(self.data.map_keys(lambda key: key ** 2), {1: 'a', 4: 'b0', 9: 'C'})
        self.checkAsDict(self.data.map_values(str.upper), {1: 'A', 2: 'B0', 3: 'C'})

    def test_len(self):
        self.assertEqual(self.data.len(), 3)

    def test_copy(self):
        copied_data = self.data.copy()
        self.assertEqual(self.data, copied_data)
        copied_data[4] = 'd'
        self.assertNotEqual(self.data, copied_data)

    def test_update(self):
        self.checkAsDict(Dict({1: 'a', 2: 'b'}).update([(3, 'c'), (4, 'd')]), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})
        self.checkAsDict(Dict({'a': 1, 'b': 2}).update(c=3, d=4), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_discard(self):
        self.checkAsDict(self.data.discard(3), {1: 'a', 2: 'b0'})
        self.checkAsDict(self.data, {1: 'a', 2: 'b0', 3: 'C'})

    def test_discard_keys(self):
        self.checkAsDict(self.data.discard_keys([1, 3]), {2: 'b0'})
        self.checkAsDict(self.data.discard(3), {1: 'a', 2: 'b0'})

    def test_each(self):
        data = Dict({'a': [1, 3], 'b': [2, 4]})
        self.checkAsDict(data.reduce_each(int.__mul__), {'a': 3, 'b': 8})
        self.checkAsDict(data.min_each(), {'a': 1, 'b': 2})
        self.checkAsDict(data.max_each(), {'a': 3, 'b': 4})
        self.checkAsDict(data.sum_each(), {'a': 4, 'b': 6})
        self.checkAsDict(data.len_each(), {'a': 2, 'b': 2})
        self.checkAsDict(data.average_each(), {'a': 2., 'b': 3.})

if __name__ == '__main__':
    unittest.main()
