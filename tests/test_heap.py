import pytest

from dsa.heap import kth_largest, top_k_frequent


class TestTopKFrequent:
    def test_basic(self):
        assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}

    def test_single(self):
        assert top_k_frequent([1], 1) == [1]

    def test_k_zero_returns_empty(self):
        assert top_k_frequent([1, 2, 3], 0) == []

    def test_ordered_by_frequency(self):
        out = top_k_frequent(["a", "a", "a", "b", "b", "c"], 3)
        assert out[0] == "a"
        assert out[1] == "b"
        assert out[2] == "c"


class TestKthLargest:
    def test_basic(self):
        assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_k_equals_n(self):
        assert kth_largest([3, 2, 1, 5, 6, 4], 6) == 1

    def test_duplicates(self):
        assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_k_too_big_raises(self):
        with pytest.raises(ValueError):
            kth_largest([1, 2], 5)

    def test_k_zero_raises(self):
        with pytest.raises(ValueError):
            kth_largest([1, 2, 3], 0)
