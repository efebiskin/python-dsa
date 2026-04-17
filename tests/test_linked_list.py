from dsa.linked_list import (
    Node,
    cycle_start,
    from_iterable,
    merge_two_sorted,
    reverse,
    to_list,
)


class TestReverse:
    def test_basic(self):
        head = from_iterable([1, 2, 3, 4, 5])
        assert to_list(reverse(head)) == [5, 4, 3, 2, 1]

    def test_single(self):
        assert to_list(reverse(from_iterable([7]))) == [7]

    def test_empty(self):
        assert reverse(None) is None


class TestMergeTwoSorted:
    def test_interleaved(self):
        a = from_iterable([1, 3, 5])
        b = from_iterable([2, 4, 6])
        assert to_list(merge_two_sorted(a, b)) == [1, 2, 3, 4, 5, 6]

    def test_one_empty(self):
        assert to_list(merge_two_sorted(None, from_iterable([1, 2]))) == [1, 2]
        assert to_list(merge_two_sorted(from_iterable([3]), None)) == [3]

    def test_both_empty(self):
        assert merge_two_sorted(None, None) is None

    def test_duplicates(self):
        a = from_iterable([1, 1, 2])
        b = from_iterable([1, 2, 2])
        assert to_list(merge_two_sorted(a, b)) == [1, 1, 1, 2, 2, 2]


class TestCycleStart:
    def test_no_cycle(self):
        head = from_iterable([1, 2, 3])
        assert cycle_start(head) is None

    def test_cycle_detected_at_correct_node(self):
        # 1 -> 2 -> 3 -> 4 -> back to 2
        n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n2
        assert cycle_start(n1) is n2

    def test_self_loop(self):
        n = Node(1)
        n.next = n
        assert cycle_start(n) is n
