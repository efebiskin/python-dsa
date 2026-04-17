# python-dsa

> 20 classic data-structure & algorithm problems in Python, organized by pattern. Every solution is production-clean, documented with its final time/space complexity, and covered by a pytest suite.

![tests](https://img.shields.io/badge/tests-80%2F80_passing-brightgreen)
![python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![problems](https://img.shields.io/badge/problems-20-blue)

This isn't a dump of LeetCode answers. Each problem is picked because it's the canonical representative of a **pattern** you need to recognize on sight. The folder structure *is* the curriculum — learn the pattern, and you can solve every variant.

---

## The 20 problems, by pattern

| # | Pattern | Problem | File | Time | Space |
|---|---------|---------|------|------|-------|
| 1 | Two Pointers | Two Sum II (sorted) | [`arrays.py`](dsa/arrays.py) | `O(n)` | `O(1)` |
| 2 | Two Pointers | 3Sum | [`arrays.py`](dsa/arrays.py) | `O(n²)` | `O(1)` |
| 3 | Two Pointers | Container With Most Water | [`arrays.py`](dsa/arrays.py) | `O(n)` | `O(1)` |
| 4 | Sliding Window | Longest Substring w/o Repeat | [`sliding_window.py`](dsa/sliding_window.py) | `O(n)` | `O(Σ)` |
| 5 | Sliding Window | Minimum Window Substring | [`sliding_window.py`](dsa/sliding_window.py) | `O(\|s\|+\|t\|)` | `O(Σ)` |
| 6 | Binary Search | Search in Rotated Sorted Array | [`binary_search.py`](dsa/binary_search.py) | `O(log n)` | `O(1)` |
| 7 | Binary Search | Find Peak Element | [`binary_search.py`](dsa/binary_search.py) | `O(log n)` | `O(1)` |
| 8 | Linked List | Reverse Linked List | [`linked_list.py`](dsa/linked_list.py) | `O(n)` | `O(1)` |
| 9 | Linked List | Merge Two Sorted Lists | [`linked_list.py`](dsa/linked_list.py) | `O(m+n)` | `O(1)` |
| 10 | Linked List | Cycle Start (Floyd's) | [`linked_list.py`](dsa/linked_list.py) | `O(n)` | `O(1)` |
| 11 | Trees / BFS | Level-Order Traversal | [`trees.py`](dsa/trees.py) | `O(n)` | `O(w)` |
| 12 | Trees / DFS | Validate BST | [`trees.py`](dsa/trees.py) | `O(n)` | `O(h)` |
| 13 | Trees / DFS | Lowest Common Ancestor | [`trees.py`](dsa/trees.py) | `O(n)` | `O(h)` |
| 14 | Heap / Top-K | Top K Frequent Elements | [`heap.py`](dsa/heap.py) | `O(n log k)` | `O(n)` |
| 15 | Heap / Top-K | Kth Largest Element | [`heap.py`](dsa/heap.py) | `O(n log k)` | `O(k)` |
| 16 | Graph / BFS | Number of Islands | [`graphs.py`](dsa/graphs.py) | `O(m·n)` | `O(min(m,n))` |
| 17 | Graph / Topo Sort | Course Schedule | [`graphs.py`](dsa/graphs.py) | `O(V+E)` | `O(V+E)` |
| 18 | DP | Longest Increasing Subsequence | [`dp.py`](dsa/dp.py) | `O(n log n)` | `O(n)` |
| 19 | DP | Coin Change | [`dp.py`](dsa/dp.py) | `O(A·C)` | `O(A)` |
| 20 | DP | Edit Distance | [`dp.py`](dsa/dp.py) | `O(mn)` | `O(min(m,n))` |

`Σ` = alphabet size · `w` = tree width · `h` = tree height · `A` = amount · `C` = coin count

---

## What's different about this repo

- **Every solution ships the *best* known approach for the problem**, not the naive one. LIS uses patience sorting (`O(n log n)`), not the `O(n²)` DP. Edit distance uses rolled `O(min(m,n))` space, not the full `O(mn)` matrix. Top-K uses `heapq.nlargest` (bounded heap) instead of sorting.
- **Every function is docstring'd with: problem statement, approach, complexity.** You can open any single file and learn the pattern cold.
- **80 pytest assertions** — not one-off examples. Edge cases included: empty inputs, single-element inputs, impossible inputs, duplicates, negative numbers, cycles.
- **Typed signatures everywhere** (`from __future__ import annotations`, `List`, `Optional`).
- **No copy-paste class wrappers** — the helpers are proper dataclasses (`Node`, `TreeNode`) with constructors that take actual arguments.

---

## Running

```bash
git clone https://github.com/efebiskin/python-dsa
cd python-dsa
pip install -e .[dev]
pytest
```

Expected output:

```
================== 80 passed in 0.06s ==================
```

---

## How to read this repo

Pick any file in [`dsa/`](dsa/). Each function has this shape:

```python
def problem_name(args) -> return_type:
    """One-line problem statement.

    Approach: the key insight, in 1-3 sentences.

    Time:  O(...)
    Space: O(...)
    """
    # implementation
```

The corresponding `tests/test_<pattern>.py` file demonstrates the function against standard inputs and the edge cases that actually trip people up (empty inputs, single elements, `k=0`, `k > n`, cycles, duplicates, impossible inputs).

---

## What I did NOT do

- I did not include trivial warmups ("reverse a string", "is palindrome"). This repo is for *patterns*, not syntax practice.
- I did not include every variant of a pattern — one representative problem per pattern. If you can solve 3Sum, you can solve 4Sum. If you can solve longest-substring-w/o-repeat, you can solve longest-repeating-character-replacement.
- I did not write brute-force solutions and then "optimize" them. Each function is the final form.

---

## License

MIT — see [LICENSE](LICENSE).
