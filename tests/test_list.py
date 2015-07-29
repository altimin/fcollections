from fcollections import List

import test_iterable

import unittest

class ListAsIterableTest(test_iterable.IterableTest):
    def setUp(self):
        self.data = List(test_iterable.data)

class ListTest(unittest.TestCase):
    def checkResult(self, result, expected):
        self.assertTrue(isinstance(result, List))
        self.assertEqual(list(result), expected)

    def test_sort(self):
        self.checkResult(List([2, 1]).sort(), [1, 2])
        self.checkResult(List([3, 1, 2]).sort(reverse=True), [3, 2, 1])

    def test_add(self):
        self.checkResult(List([1, 2]) + List([3, 4]), [1, 2, 3, 4])
        self.checkResult([1, 2] + List([3, 4]), [1, 2, 3, 4])
        self.checkResult(List([1, 2]) + [3, 4], [1, 2, 3, 4])

    def test_mul(self):
        self.checkResult(List([1, 2]) * 2, [1, 2, 1, 2])
        self.checkResult(2 * List([1, 2]), [1, 2, 1, 2])

if __name__ == '__main__':
    unittest.main()
