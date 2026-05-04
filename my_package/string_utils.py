"""
A collection of string utility functions for common string manipulation
and analysis tasks.
"""


def reverse_string(s: str) -> str:
    """
    Return the reversed version of a string.

    Args:
        s: The input string to reverse.

    Returns:
        A new string with the characters of `s` in reverse order.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring case and spaces.

    A palindrome reads the same forwards and backwards. This function
    normalises the input by converting it to lowercase and stripping all
    spaces before performing the check.

    Args:
        s: The input string to check.

    Returns:
        True if `s` is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    normalised = s.lower().replace(" ", "")
    return normalised == normalised[::-1]


def word_count(s: str) -> dict:
    """
    Return a dictionary of word frequencies for the given string.

    The comparison is case-insensitive; all words are lowercased before
    counting. Punctuation is *not* stripped — only whitespace is used as
    the delimiter.

    Args:
        s: The input string to analyse.

    Returns:
        A dictionary mapping each unique word (lowercase) to the number
        of times it appears in `s`.

    Examples:
        >>> word_count("the cat sat on the mat")
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
        >>> word_count("Hello hello HELLO")
        {'hello': 3}
    """
    frequencies: dict = {}
    for word in s.lower().split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
