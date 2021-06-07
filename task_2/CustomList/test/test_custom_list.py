
import unittest

from custom_list import CustomList

class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([1, 2, 3])

    def test_neg(self):
        self.assertEqual(-self.custom_list, CustomList([-1, -2, -3]))
        self.assertEqual(-CustomList([]), CustomList([]))

    def test_add(self):
        self.assertEqual(self.custom_list + [0, -2, 4, 8], CustomList([1, 0, 7, 8]))
        self.assertEqual(self.custom_list + [], self.custom_list)
        self.assertEqual(self.custom_list + [3, 5, 6], CustomList([4, 7, 9]))
        self.assertEqual(self.custom_list + CustomList([1, -1, 2, 6]), CustomList([2, 1, 5, 6]))

    def test_radd(self):
        self.assertEqual([-3, 5] + self.custom_list, CustomList([-2, 7, 3]))
        self.assertEqual([] + self.custom_list, self.custom_list)
        self.assertEqual([3, 3, 8, 1] + self.custom_list, CustomList([4, 5, 11, 1]))
        self.assertEqual(CustomList([1]) + self.custom_list, CustomList([2, 2, 3]))

    def test_sub(self):
        self.assertEqual(self.custom_list - [3, 2, 1], CustomList([-2, 0, 2]))
        self.assertEqual(self.custom_list - [], self.custom_list)
        self.assertEqual(self.custom_list - [-1, -2], CustomList([2, 4, 3]))
        self.assertEqual(self.custom_list - CustomList([3, 1, 9, 3]), CustomList([-2, 1, -6, -3]))

    def test_rsub(self):
        self.assertEqual([] - self.custom_list, CustomList([-1, -2, -3]))
        self.assertEqual([2, 8, 12, 3] - self.custom_list, CustomList([1, 6, 9, 3]))
        self.assertEqual([10, 7] - self.custom_list, CustomList([9, 5, -3]))
        self.assertEqual(CustomList([8, 7]) - self.custom_list, CustomList([7, 5, -3]))

    def test_immutability(self):
        self.assertEqual(self.custom_list + [0, -2, 4, 8], CustomList([1, 0, 7, 8]))
        self.assertEqual(self.custom_list, CustomList([1, 2, 3]))

        self.assertEqual([-3, 5] + self.custom_list, CustomList([-2, 7, 3]))
        self.assertEqual(self.custom_list, CustomList([1, 2, 3]))

        self.assertEqual(self.custom_list - [3, 2, 1], CustomList([-2, 0, 2]))
        self.assertEqual(self.custom_list, CustomList([1, 2, 3]))

        self.assertEqual([2, 8, 12, 3] - self.custom_list, CustomList([1, 6, 9, 3]))
        self.assertEqual(self.custom_list, CustomList([1, 2, 3]))

    def test_comp(self):
        self.assertEqual(CustomList([2, 8, 1]), CustomList([3, 6, 2]))
        self.assertNotEqual(CustomList([-1, 3, 5]), CustomList([2, 3]))
        self.assertGreater(CustomList([1, 4, 5]), CustomList([]))
        self.assertGreaterEqual(CustomList([]), CustomList([2, -2]))
        self.assertLess(CustomList([1, 2, 1]), CustomList([2, 3, 4]))
        self.assertLessEqual(CustomList([3]), CustomList([6, 7]))

if __name__ == "__main__":
    unittest.main()
