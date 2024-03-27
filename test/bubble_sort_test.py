import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):


    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble_sort([5,5,7,8,2,4,1]), [1,2,4,5,5,7,8])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_with_negative_numbers(self):
        self.assertEqual(bubble_sort([-5,-5,-7,-8,-2,-4,-1]), [-8,-7,-5,-5,-4,-2,-1])

    def test_bubble_sort_with_mixed_numbers(self):
        self.assertEqual(bubble_sort([5,-5,7,-8,2,-4,1]), [-8,-5,-4,1,2,5,7])
        
if __name__ == '__main__':
    unittest.main(verbosity=2)