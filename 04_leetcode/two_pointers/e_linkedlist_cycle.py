"""
Problem: 141. Linked List Cycle
URL: https://leetcode.com/problems/linked-list-cycle/description/
Difficulty: [Easy]
Pattern: two pointers slow/fast

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False