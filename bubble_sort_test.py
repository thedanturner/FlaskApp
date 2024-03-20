import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):


    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble_sort([5,5,7,8,2,4,1]), [1,2,4,5,5,7,8])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)