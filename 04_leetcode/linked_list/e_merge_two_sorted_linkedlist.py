"""
Problem: 21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
Difficulty: [Easy]
Pattern: two pointers

Time Complexity: O(n+m) because we iterate through the nodes one by one,
while linking the leftover chain at the end happens instantly in $O(1)$ constant time.
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Setup your anchor points
        dummy = ListNode()
        tail = dummy

        # 2. Loop while BOTH lists still have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                # Connect the tail's next pointer to list1
                tail.next = list1
                # Move list1's pointer to its next node
                list1 = list1.next  # Move list1's head forward

            else:
                # Connect the tail's next pointer to list2
                tail.next = list2  # Link tail to list2's current node
                # Move list2's pointer to its next node
                list2 = list2.next  # Move list2's head forward

            # Move the tail forward by one node so it's ready for the next link
            tail = tail.next

        # 3. Clean up the leftovers
        # One list is now empty. Attach the remaining non-empty list directly to tail.next
        if list1:
            # Link tail to the rest of list1
            tail.next = list1
        elif list2:
            # Link tail to the rest of list2
            tail.next = list2

        # 4. Return the head of the merged list
        # Hint: It's not 'dummy' itself, but what comes right after it
        return dummy.next

# SOLUTION 2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 1. Create a dummy node as a stable anchor, and use 'tail' as our
        #    construction worker pointer tracking the end of our new list.
        dummy = ListNode(0)
        tail = dummy

        # 2. Loop while both lists still have nodes left to compare.
        while list1 and list2:
            # Pick the smaller value from the front of the lists
            if list1.val <= list2.val:
                tail.next = list1  # Hook tail to list1's current node
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2  # Hook tail to list2's current node
                list2 = list2.next  # Move list2 pointer forward

            # Move our construction worker (tail) forward to the newly attached node
            tail = tail.next

        # 3. Attach any leftover nodes from whichever list still has items
        tail.next = list1 or list2

        # 4. Skip the fake dummy node at the start and return the true head of our merged list
        return dummy.next