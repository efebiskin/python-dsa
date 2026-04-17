from dsa.sliding_window import longest_substring_no_repeat, min_window_substring


class TestLongestSubstringNoRepeat:
    def test_basic(self):
        assert longest_substring_no_repeat("abcabcbb") == 3  # "abc"

    def test_all_same(self):
        assert longest_substring_no_repeat("bbbbb") == 1

    def test_mixed(self):
        assert longest_substring_no_repeat("pwwkew") == 3  # "wke"

    def test_empty(self):
        assert longest_substring_no_repeat("") == 0

    def test_full_unique(self):
        assert longest_substring_no_repeat("abcdef") == 6


class TestMinWindowSubstring:
    def test_basic(self):
        assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"

    def test_exact(self):
        assert min_window_substring("a", "a") == "a"

    def test_impossible(self):
        assert min_window_substring("a", "aa") == ""

    def test_empty_t(self):
        assert min_window_substring("hello", "") == ""

    def test_handles_repeated_chars_in_t(self):
        assert min_window_substring("aaflslflsldkalskaaa", "aaa") == "aaa"
