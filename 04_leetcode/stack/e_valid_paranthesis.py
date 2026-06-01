"""
Problem: 20. Valid Parantheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

URL: https://leetcode.com/problems/valid-parentheses/description/
Difficulty: [Easy]
Pattern: stack (LIFO)

Time Complexity: O(n) bc work scales linearly with size of input string
Space Complexity: O(n) bc space of stack can grow if not given ending bracket
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for chara in s:
            if chara in "([{":
                stack.append(chara)
            elif chara in "}])":
                if not stack:
                    return False

                # if they match pop
                top_item = stack.pop()

                # check if opening and closing bracket match
                if chara == ")" and top_item != "(":
                    return False
                if chara == "]" and top_item != "[":
                    return False
                if chara == "}" and top_item != "{":
                    return False

        return not stack