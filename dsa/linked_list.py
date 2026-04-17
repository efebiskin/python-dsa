"""Linked-list problems."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None


def from_iterable(xs: Iterable[int]) -> Optional[Node]:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    for x in xs:
        n = Node(x)
        if head is None:
            head = tail = n
        else:
            assert tail is not None
            tail.next = n
            tail = n
    return head


def to_list(head: Optional[Node]) -> List[int]:
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def reverse(head: Optional[Node]) -> Optional[Node]:
    """Reverse a singly linked list in place.

    Approach: iterative pointer flip — keep prev, curr; redirect curr.next
    back to prev each step.

    Time:  O(n)
    Space: O(1)
    """
    prev: Optional[Node] = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def merge_two_sorted(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    """Merge two sorted singly linked lists.

    Approach: dummy head + tail pointer. Splice whichever input head is
    smaller, advance, repeat. Attach leftover tail at the end.

    Time:  O(m + n)
    Space: O(1)
    """
    dummy = Node(0)
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next


def cycle_start(head: Optional[Node]) -> Optional[Node]:
    """Detect cycle start (Floyd's tortoise and hare).

    Returns the node where the cycle begins, or None if no cycle.

    Approach: advance slow 1 step and fast 2 steps; if they meet, reset slow
    to head and advance both 1 step at a time — they meet at the cycle entry.
    This falls out of the arithmetic where the remaining distance from the
    meeting point to the cycle entry equals the distance from the head to
    the cycle entry (mod cycle length).

    Time:  O(n)
    Space: O(1)
    """
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Phase 2: find entry.
            p = head
            while p is not slow:
                assert p is not None and slow is not None
                p = p.next
                slow = slow.next
            return p
    return None
