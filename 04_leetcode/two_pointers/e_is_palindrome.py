"""
Problem: Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
URL: https://neetcode.io/problems/is-palindrome/question
Difficulty: [Easy]
Pattern: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            if (not 97 <= ord(s[L]) <= 122
                and not 65 <= ord(s[L]) <= 90
                and not 48 <= ord(s[L]) <= 57):
                L += 1
                continue
            if (not 97 <= ord(s[R]) <= 122
                and not 65 <= ord(s[R]) <= 90
                and not 48 <= ord(s[R]) <= 57):
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1

        return True

"""
Another solution:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Start with an empty list to hold our valid characters
        chars = []

        # Step 2: Loop through every character in the original string
        for char in s:
            # Step 3: If it's a letter or a number, lowercase it and save it
            if char.isalnum():
                chars.append(char.lower())

        # Step 4: Turn our list back into a clean string
        cleaned = "".join(chars)

        # Step 5: Set up our pointers at the very beginning and very end
        left = 0
        right = len(cleaned) - 1

        # Step 6: Walk both pointers inward to check for a match
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        # Step 7: If everything matches, it's a palindrome!
        return True