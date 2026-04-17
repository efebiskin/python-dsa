import pytest

from dsa.arrays import container_with_most_water, three_sum, two_sum_sorted


class TestTwoSumSorted:
    def test_basic(self):
        assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)

    def test_middle(self):
        assert two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3)

    def test_negatives(self):
        # Two valid pairs exist: (0,3) -3+2 and (1,2) -1+0. The two-pointer
        # scan finds (0,3) first because it starts at both ends.
        assert two_sum_sorted([-3, -1, 0, 2, 4], -1) == (0, 3)

    def test_no_pair_raises(self):
        with pytest.raises(ValueError):
            two_sum_sorted([1, 2, 3], 100)


class TestThreeSum:
    def test_standard(self):
        assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]

    def test_all_zeros(self):
        assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]

    def test_no_triplet(self):
        assert three_sum([1, 2, 3]) == []

    def test_handles_duplicates(self):
        result = three_sum([-2, 0, 0, 2, 2])
        assert result == [[-2, 0, 2]]


class TestContainerWithMostWater:
    def test_example(self):
        assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_monotonic(self):
        assert container_with_most_water([1, 2, 3, 4, 5]) == 6

    def test_single_pair(self):
        assert container_with_most_water([4, 3]) == 3
