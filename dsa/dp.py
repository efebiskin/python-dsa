"""Dynamic-programming problems."""
from __future__ import annotations

from bisect import bisect_left
from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """Length of the longest *strictly* increasing subsequence.

    Approach: patience sorting. Maintain `tails[k]` = the smallest possible
    tail of any increasing subsequence of length k+1 seen so far. For each
    value, binary-search its position in `tails` and either replace or append.

    Time:  O(n log n)
    Space: O(n)
    """
    tails: List[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def coin_change(coins: List[int], amount: int) -> int:
    """Fewest coins to make `amount`, or -1 if impossible.

    Approach: 1D DP. dp[a] = min coins to make a. Initialize dp[0] = 0, the
    rest to infinity. For each sub-amount a, try every coin: if dp[a - c]
    is reachable, dp[a] = min(dp[a], dp[a - c] + 1).

    Time:  O(amount * len(coins))
    Space: O(amount)
    """
    if amount < 0:
        return -1
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return -1 if dp[amount] == INF else int(dp[amount])


def edit_distance(a: str, b: str) -> int:
    """Levenshtein edit distance between `a` and `b`.

    Edits allowed: insert, delete, replace (each cost 1).

    Approach: classic 2D DP rolled into two 1D rows.
      dp[i][j] = edit(a[:i], b[:j])
      transitions: (insert) dp[i][j-1] + 1
                   (delete) dp[i-1][j] + 1
                   (replace/match) dp[i-1][j-1] + (a[i-1] != b[j-1])

    Time:  O(|a| * |b|)
    Space: O(min(|a|, |b|))
    """
    if len(a) < len(b):
        a, b = b, a  # ensure b is the shorter (tighter space bound)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            curr[j] = min(
                curr[j - 1] + 1,          # insert
                prev[j] + 1,              # delete
                prev[j - 1] + cost,       # match or replace
            )
        prev = curr
    return prev[len(b)]
