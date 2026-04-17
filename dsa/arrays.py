"""Arrays / two-pointer problems."""
from __future__ import annotations

from typing import List, Tuple


def two_sum_sorted(nums: List[int], target: int) -> Tuple[int, int]:
    """Two Sum II — input array is sorted.

    Return the 0-indexed pair (i, j) with i < j and nums[i] + nums[j] == target.
    Raises ValueError if no such pair exists.

    Approach: two pointers from both ends. If the sum is too small, move left
    pointer right (increase); if too large, move right pointer left (decrease).

    Time:  O(n)
    Space: O(1)
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return lo, hi
        if s < target:
            lo += 1
        else:
            hi -= 1
    raise ValueError("no pair sums to target")


def three_sum(nums: List[int]) -> List[List[int]]:
    """3Sum: all unique triplets (a, b, c) in `nums` with a + b + c == 0.

    Approach: sort, then for each anchor index i, run a two-pointer scan over
    the suffix nums[i+1:]. Skip duplicates at each pointer to keep output
    triplets unique.

    Time:  O(n^2)
    Space: O(1) extra (output excluded)
    """
    nums = sorted(nums)
    n = len(nums)
    out: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break  # all remaining values are positive, can't sum to 0
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate anchors
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s == 0:
                out.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return out


def container_with_most_water(heights: List[int]) -> int:
    """Container with most water.

    Given non-negative integers representing wall heights, find two lines that
    form a container holding the most water (area = min(h_i, h_j) * (j - i)).

    Approach: two pointers. The limiting wall is the shorter one; moving the
    taller inward can only shrink area, so always move the shorter one.

    Time:  O(n)
    Space: O(1)
    """
    lo, hi = 0, len(heights) - 1
    best = 0
    while lo < hi:
        area = min(heights[lo], heights[hi]) * (hi - lo)
        if area > best:
            best = area
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return best
