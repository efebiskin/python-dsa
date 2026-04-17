from dsa.graphs import course_schedule, num_islands


class TestNumIslands:
    def test_empty(self):
        assert num_islands([]) == 0
        assert num_islands([[]]) == 0

    def test_single_island(self):
        grid = [
            ["1", "1", "0"],
            ["1", "0", "0"],
            ["0", "0", "0"],
        ]
        assert num_islands([row[:] for row in grid]) == 1

    def test_three_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert num_islands([row[:] for row in grid]) == 3

    def test_diagonal_is_not_connected(self):
        grid = [
            ["1", "0"],
            ["0", "1"],
        ]
        assert num_islands([row[:] for row in grid]) == 2


class TestCourseSchedule:
    def test_no_prereqs(self):
        assert course_schedule(3, []) is True

    def test_simple_chain(self):
        assert course_schedule(2, [[1, 0]]) is True

    def test_cycle_rejected(self):
        assert course_schedule(2, [[1, 0], [0, 1]]) is False

    def test_large_acyclic(self):
        prereqs = [[1, 0], [2, 1], [3, 2], [4, 2]]
        assert course_schedule(5, prereqs) is True

    def test_long_cycle(self):
        prereqs = [[0, 1], [1, 2], [2, 3], [3, 0]]
        assert course_schedule(4, prereqs) is False
