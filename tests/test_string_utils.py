import unittest
from utils.string_utils import (
    count_spaces, is_sorted_str, is_palindrome_str,
    to_lowercase, to_uppercase, swap_case, to_titlecase,
    extract_substring, find_substring, replace_char, compare_strings
)

class TestStringUtils(unittest.TestCase):
    def test_count_spaces(self):
        self.assertEqual(count_spaces("hello world"), 1)
        self.assertEqual(count_spaces("   "), 3)
        self.assertEqual(count_spaces("nospaces"), 0)

    def test_is_sorted_str(self):
        self.assertTrue(is_sorted_str("abc"))
        self.assertTrue(is_sorted_str("aabbcc"))
        self.assertFalse(is_sorted_str("cba"))
        self.assertFalse(is_sorted_str("aba"))

    def test_is_palindrome_str(self):
        self.assertTrue(is_palindrome_str("racecar"))
        self.assertTrue(is_palindrome_str(""))
        self.assertFalse(is_palindrome_str("hello"))

    def test_case_conversions(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Hello 123!"), "hello 123!")
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Hello 123!"), "HELLO 123!")
        self.assertEqual(swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(to_titlecase("hello world of python"), "Hello World Of Python")

    def test_extract_substring(self):
        self.assertEqual(extract_substring("abcdef", 2, 5), "cde")

    def test_find_substring(self):
        self.assertTrue(find_substring("hello world", "world"))
        self.assertTrue(find_substring("hello world", ""))
        self.assertFalse(find_substring("hello world", "python"))

    def test_replace_char(self):
        self.assertEqual(replace_char("banana", "a", "o"), "bonono")

    def test_compare_strings(self):
        self.assertTrue(compare_strings("hello", "hello"))
        self.assertFalse(compare_strings("hello", "world"))

if __name__ == "__main__":
    unittest.main()
