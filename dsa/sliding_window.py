"""Sliding-window problems."""
from __future__ import annotations

from collections import Counter


def longest_substring_no_repeat(s: str) -> int:
    """Longest substring without repeating characters.

    Approach: expanding-right, contracting-left window. A dict maps char to
    its latest index; when a duplicate enters, jump the left edge past its
    previous occurrence.

    Time:  O(n)
    Space: O(min(n, alphabet))
    """
    last: dict[str, int] = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best


def min_window_substring(s: str, t: str) -> str:
    """Minimum window substring.

    Return the shortest contiguous slice of `s` that contains every character
    of `t` with at least the required multiplicity. Empty string if impossible.

    Approach: expand right to accumulate requirements; once all are met,
    contract left while the window is still valid. Track best seen.

    Time:  O(|s| + |t|)
    Space: O(alphabet)
    """
    if not t or len(s) < len(t):
        return ""

    need = Counter(t)
    missing = len(t)  # total count still needed (with multiplicities)
    left = 0
    best_lo, best_len = 0, -1

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if best_len == -1 or right - left + 1 < best_len:
                best_lo, best_len = left, right - left + 1
            # Release the leftmost char so we keep searching for smaller windows.
            need[s[left]] += 1
            missing += 1
            left += 1

    return "" if best_len == -1 else s[best_lo:best_lo + best_len]
