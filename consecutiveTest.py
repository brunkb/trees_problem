import unittest

from consecutive import findtotalConsecutive

class TestConsecutive(unittest.TestCase):
    def test_findtotalConsecutive(self):
        """Test that this function finds the max sum in a list of integers"""
        treesList = [1, 2, 5, 3]
        result = findtotalConsecutive(treesList, 2, 2)
        self.assertEqual(result, 8)

    def test_findtotalConsecutive(self):
        """Test that this function returns -1 when index and size are not supported by the input array"""
        treesList = [1, 2, 5, 3]
        result = findtotalConsecutive(treesList, 2, 4)
        self.assertEqual(result, -1)

    def test_findtotalConsecutive(self):
        """Basic success test"""
        treesList = [0, 1, 0, 0]  # answer should be 1
        result = findtotalConsecutive(treesList, 1, 1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
