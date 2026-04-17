"""Binary-tree problems."""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Binary-tree level-order (BFS) traversal.

    Approach: queue of nodes, popped one level at a time. Snapshot the
    queue length at the start of each level so we know when it ends.

    Time:  O(n)
    Space: O(width)  (max queue size = maximum tree width)
    """
    if root is None:
        return []
    out: List[List[int]] = []
    q: deque[TreeNode] = deque([root])
    while q:
        level: List[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left is not None: q.append(node.left)
            if node.right is not None: q.append(node.right)
        out.append(level)
    return out


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Check if a binary tree is a valid BST.

    The BST invariant is GLOBAL, not just "left.val < node.val < right.val"
    between a node and its immediate children — every value in the left
    subtree must be strictly less than node.val, etc.

    Approach: DFS with a running (lo, hi) open interval that tightens as we
    descend. Each node must lie strictly in (lo, hi).

    Time:  O(n)
    Space: O(h)  recursion stack
    """
    def walk(n: Optional[TreeNode], lo: float, hi: float) -> bool:
        if n is None:
            return True
        if not (lo < n.val < hi):
            return False
        return walk(n.left, lo, n.val) and walk(n.right, n.val, hi)

    return walk(root, float("-inf"), float("inf"))


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Lowest common ancestor in a binary tree.

    Approach: post-order DFS. A node is the LCA iff one target is found in
    its left subtree and the other in its right subtree, OR the node itself
    is one of the targets and the other is in either subtree.

    Time:  O(n)
    Space: O(h)
    """
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right
