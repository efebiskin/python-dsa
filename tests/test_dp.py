from dsa.dp import coin_change, edit_distance, longest_increasing_subsequence


class TestLIS:
    def test_standard(self):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        # [2, 3, 7, 101] or [2, 3, 7, 18]

    def test_all_same(self):
        assert longest_increasing_subsequence([7, 7, 7, 7]) == 1

    def test_empty(self):
        assert longest_increasing_subsequence([]) == 0

    def test_strictly_increasing(self):
        assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero_amount(self):
        assert coin_change([1, 2, 5], 0) == 0

    def test_exact_coin(self):
        assert coin_change([1, 2, 5], 5) == 1


class TestEditDistance:
    def test_kitten_sitting(self):
        assert edit_distance("kitten", "sitting") == 3

    def test_empty_target(self):
        assert edit_distance("abc", "") == 3
        assert edit_distance("", "xyz") == 3

    def test_equal(self):
        assert edit_distance("same", "same") == 0

    def test_insert_only(self):
        assert edit_distance("cat", "cats") == 1

    def test_replace_only(self):
        assert edit_distance("cat", "bat") == 1
