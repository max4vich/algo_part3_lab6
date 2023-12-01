import unittest

from src.find_substring import find_substring


class TestFindSubstringIndices(unittest.TestCase):
    def test_with_space_find_substring_indices(self):
        self.assertEqual(find_substring("hello world", "world"), [6])

    def test_double_repeat_find_substring_indices(self):
        self.assertEqual(find_substring("абракадабра", "абра"), [0, 7])

    def test_without_return_find_substring_indices(self):
        self.assertEqual(find_substring("hello world", "goodbye"), [])

    def test_double_a_find_substring_indices(self):
        self.assertEqual(find_substring("aaaaa", "aa"), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
