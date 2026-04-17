from dsa.binary_search import find_peak_element, search_rotated


class TestSearchRotated:
    def test_found_in_right_half(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_found_in_left_half(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1

    def test_missing(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_not_rotated(self):
        assert search_rotated([1, 2, 3, 4, 5], 4) == 3

    def test_single(self):
        assert search_rotated([1], 1) == 0
        assert search_rotated([1], 0) == -1

    def test_empty(self):
        assert search_rotated([], 1) == -1


class TestFindPeakElement:
    def test_any_peak(self):
        idx = find_peak_element([1, 2, 3, 1])
        assert idx == 2  # unique peak at 3

    def test_monotonic_ascending(self):
        # Peak is the last element (neighbour past the end = -inf).
        assert find_peak_element([1, 2, 3, 4, 5]) == 4

    def test_monotonic_descending(self):
        assert find_peak_element([5, 4, 3, 2, 1]) == 0

    def test_two_peaks_either_valid(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(nums)
        assert idx in {1, 5}
