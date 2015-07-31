from fcollections import List
from fcollections import Iterable

import tests.test_iterable as test_iterable

import unittest

class ListAsIterableTest(test_iterable.IterableTest):
    def setUp(self):
        self.data = List(test_iterable.data)

class ListTest(unittest.TestCase):
    def checkResult(self, result, expected, expected_type=List):
        self.assertTrue(isinstance(result, expected_type))
        self.assertEqual(list(result), expected)

    def test_sort(self):
        # .sorted() returns new list, leaving old unchanged
        list1 = List([2, 1])
        self.checkResult(list1.sorted(), [1, 2])
        self.checkResult(list1, [2, 1])

        # .sort() sorts list inplace, returning self
        list2 = List([2, 1])
        self.checkResult(list2.sort(), [1, 2])
        self.checkResult(list2, [1, 2])

        self.checkResult(List([3, 1, 2]).sort(reverse=True), [3, 2, 1])

    def test_reversed(self):
        # .reversed() returns iterable without actually changing list
        list1 = List([2, 1])
        self.checkResult(list1.reversed(), [1, 2], expected_type=Iterable)
        self.checkResult(list1, [2, 1])

        # .reverse() reverses list inplace and returns self
        list2 = List([2, 1])
        self.checkResult(list2.reverse(), [1, 2])
        self.checkResult(list2, [1, 2])

    def test_add(self):
        self.checkResult(List([1, 2]) + List([3, 4]), [1, 2, 3, 4])
        self.checkResult([1, 2] + List([3, 4]), [1, 2, 3, 4])
        self.checkResult(List([1, 2]) + [3, 4], [1, 2, 3, 4])

    def test_mul(self):
        self.checkResult(List([1, 2]) * 2, [1, 2, 1, 2])
        self.checkResult(2 * List([1, 2]), [1, 2, 1, 2])

    def test_slice(self):
        data = List([1, 2, 3, 4, 5])
        self.checkResult(data[1:], [2, 3, 4, 5])
        self.checkResult(data[:-1], [1, 2, 3, 4])
        self.checkResult(data[::2], [1, 3, 5])

if __name__ == '__main__':
    unittest.main()
