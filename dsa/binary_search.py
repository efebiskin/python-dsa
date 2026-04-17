"""Binary-search problems (beyond vanilla search)."""
from __future__ import annotations

from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    """Search in a rotated sorted array.

    The input was originally sorted ascending, then rotated at some unknown
    pivot. Return the index of `target`, or -1 if absent.

    Approach: modified binary search. At each step, one of the two halves is
    definitely sorted (the mid compared to the left end tells us which). If
    target falls inside the sorted half, recurse there; otherwise the other.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            # Left half is sorted.
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # Right half is sorted.
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_peak_element(nums: List[int]) -> int:
    """Find a peak element (any index where nums[i] > its neighbours).

    Edges count as -∞ so the first and last indices can be peaks.

    Approach: binary search. Compare nums[mid] with nums[mid+1]. If ascending,
    a peak must be to the right (or at mid+1). If descending, to the left
    (or at mid). Narrow the window until lo == hi.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo
