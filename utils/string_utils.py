"""Custom string utility functions replacing the legacy class string methods."""

def count_spaces(s: str) -> int:
    """Return the count of spaces in a string."""
    return s.count(' ')

def is_sorted_str(s: str) -> bool:
    """Check if characters in a string are in non-decreasing lexicographical order."""
    return all(s[i] <= s[i+1] for i in range(len(s) - 1))

def is_palindrome_str(s: str) -> bool:
    """Check if a string reads the same backwards as forwards."""
    return s == s[::-1]

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase using standard ascii arithmetic (from scratch style)."""
    return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase using standard ascii arithmetic."""
    return "".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s)

def swap_case(s: str) -> str:
    """Swap character casing using ascii calculations."""
    return "".join(
        chr(ord(c) + 32) if 'A' <= c <= 'Z' else
        chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        for c in s
    )

def to_titlecase(s: str) -> str:
    """Convert string to titlecase (capitalize first letter of each word)."""
    words = s.split(' ')
    title_words = []
    for w in words:
        if not w:
            title_words.append('')
            continue
        first = w[0]
        rest = w[1:]
        first_up = chr(ord(first) - 32) if 'a' <= first <= 'z' else first
        rest_low = "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in rest)
        title_words.append(first_up + rest_low)
    return " ".join(title_words)

def extract_substring(s: str, start: int, end: int) -> str:
    """Extract a substring from index `start` to `end` (exclusive)."""
    return s[start:end]

def find_substring(s1: str, s2: str) -> bool:
    """Search for the existence of substring `s2` in `s1`."""
    if not s2:
        return True
    n1, n2 = len(s1), len(s2)
    for i in range(n1 - n2 + 1):
        if s1[i:i+n2] == s2:
            return True
    return False

def replace_char(s: str, old: str, new: str) -> str:
    """Replace occurrences of character `old` with `new`."""
    return "".join(new if c == old else c for c in s)

def compare_strings(s1: str, s2: str) -> bool:
    """Compare two strings for equality."""
    return s1 == s2
