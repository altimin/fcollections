import unittest

from fcollections import Iterable

data = [5, 2, 3, 2, 1]

class IterableTest(unittest.TestCase):
    def setUp(self):
        self.data = Iterable(item for item in data)

    def checkResult(self, result, expected):
        self.assertTrue(isinstance(result, Iterable))
        self.assertEqual(list(result), expected)

    def test_basic(self):
        self.assertEqual(data, list(self.data))

    def test_count1(self):
        self.assertEqual(self.data.count(2), 2)

    def test_count2(self):
        self.assertEqual(self.data.count(5), 1)

    def test_count3(self):
        self.assertEqual(self.data.count(0), 0)

    def test_count4(self):
        self.assertEqual(self.data.count(), { 1: 1, 2: 2, 3: 1, 5: 1})

    def test_sort(self):
        self.assertEqual(self.data.sort(), sorted(data))

    def test_filter(self):
        self.checkResult(self.data.filter(lambda x: x > 2), [5, 3])

    def test_map(self):
        self.checkResult(self.data.map(lambda x: x % 2), [1, 0, 1, 0, 1])

    def test_starmap(self):
        data = [(3, 4), (5, -1), (8, 0)]
        self.checkResult(Iterable(data).starmap(lambda x, y: x + y), [7, 4, 8])

    def test_doublestarmap(self):
        data = [{'x': 3, 'y': 4}, {'x': 5, 'y': -1}, {'x': 8, 'y': 0}]
        self.checkResult(Iterable(data).doublestarmap(lambda x, y: x + y), [7, 4, 8])

    def test_reduce1(self):
        self.assertEqual(self.data.reduce(lambda x, y: x + y), 13)

    def test_reduce2(self):
        self.assertEqual(self.data.reduce(lambda x, y: x + y, 10), 23)

    def test_reduce3(self):
        self.assertEqual(Iterable([]).reduce(lambda x, y: x + y, -1), -1)

    def test_groupby(self):
        self.assertEqual(self.data.groupby(lambda x: x % 3), {0: [3], 1: [1], 2: [5, 2, 2]})

    def test_len(self):
        self.assertEqual(self.data.len(), 5)

    def test_max(self):
        self.assertEqual(self.data.max(), 5)

    def test_min(self):
        self.assertEqual(self.data.min(), 1)

    def test_sum(self):
        self.assertEqual(self.data.sum(), 13)

    def test_all(self):
        self.assertEqual(Iterable([True, False]).all(), False)
        self.assertEqual(Iterable([True, True]).all(), True)

    def test_any(self):
        self.assertEqual(Iterable([True, False]).any(), True)
        self.assertEqual(Iterable([False, False]).any(), False)

    def test_take(self):
        self.checkResult(self.data.take(3), [5, 2, 3])

    def test_drop(self):
        self.checkResult(self.data.drop(3), [2, 1])

    def test_takewhile(self):
        self.checkResult(self.data.takewhile(lambda x: x != 3), [5, 2])

    def test_takeuntil(self):
        self.checkResult(self.data.takeuntil(lambda x: x == 1), [5, 2, 3, 2])

    def test_dropwhile(self):
        self.checkResult(self.data.dropwhile(lambda x: x != 3), [3, 2, 1])

    def test_dropuntil(self):
        self.checkResult(self.data.dropuntil(lambda x: x == 1), [1])

    def test_unique(self):
        self.checkResult(self.data.unique(), [5, 2, 3, 1])

if __name__ == '__main__':
    unittest.main()
