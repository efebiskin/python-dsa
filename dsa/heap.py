"""Heap / top-K problems."""
from __future__ import annotations

import heapq
from collections import Counter
from typing import Iterable, List


def top_k_frequent(nums: Iterable[int], k: int) -> List[int]:
    """Top K most frequent elements.

    Approach: Counter + heapq.nlargest on frequency. nlargest uses a bounded
    min-heap of size k, giving O(n log k) rather than O(n log n) of a full sort.

    Time:  O(n log k)
    Space: O(n)
    """
    if k <= 0:
        return []
    counts = Counter(nums)
    return [val for val, _ in counts.most_common(k)]


def kth_largest(nums: Iterable[int], k: int) -> int:
    """Kth largest element.

    Approach: maintain a min-heap of size k. The root is always the kth
    largest seen so far; push each new value and pop if size exceeds k.

    Time:  O(n log k)
    Space: O(k)
    """
    if k <= 0:
        raise ValueError("k must be positive")
    heap: List[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    if len(heap) < k:
        raise ValueError("fewer than k elements given")
    return heap[0]
