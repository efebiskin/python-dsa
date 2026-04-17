"""Graph problems (grid + directed graph)."""
from __future__ import annotations

from collections import defaultdict, deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Number of connected "1" components in a 2D grid.

    "1" is land, "0" is water. Horizontal and vertical adjacency only.

    Approach: iterate cells; when we hit unvisited land, BFS-flood it to
    mark the whole component as visited in-place.

    Time:  O(m * n)
    Space: O(min(m, n))  BFS frontier bound
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            q: deque[tuple[int, int]] = deque([(r, c)])
            grid[r][c] = "#"
            while q:
                y, x = q.popleft()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == "1":
                        grid[ny][nx] = "#"
                        q.append((ny, nx))
    return islands


def course_schedule(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Course schedule: can all courses be finished?

    prerequisites[i] = [a, b] means to take a you must first take b. Return
    True iff the graph has no cycle.

    Approach: Kahn's algorithm (BFS topological sort). Track in-degrees;
    pop zero-degree nodes; decrement neighbours. If we pop all n nodes,
    no cycle — otherwise there's one.

    Time:  O(V + E)
    Space: O(V + E)
    """
    graph: dict[int, list[int]] = defaultdict(list)
    in_deg = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        in_deg[a] += 1

    q: deque[int] = deque(i for i in range(num_courses) if in_deg[i] == 0)
    taken = 0
    while q:
        node = q.popleft()
        taken += 1
        for nxt in graph[node]:
            in_deg[nxt] -= 1
            if in_deg[nxt] == 0:
                q.append(nxt)
    return taken == num_courses
