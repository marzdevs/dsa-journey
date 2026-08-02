"""
Problem: 424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
URL: 
Difficulty: [Medium]
Pattern: sliding window / hashmap

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        maxf = 0
        max_length = 0

        for right in range(len(s)):
            # checks if it exists otherwise update
            counts[s[right]] = counts.get(s[right], 0) + 1
            # see if new count is largest and max picks largest from the two
            maxf = max(maxf, counts[s[right]])

            while ( (right - left + 1) - maxf) > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length

# ANOTHER SOLUTION
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_state = {}
        max_len = 0

        # Expand the window by moving the 'right' pointer across the string
        for right in range(len(s)):
            # 1. Add current character into our window count dictionary
            char = s[right]
            window_state[char] = window_state.get(char, 0) + 1

            # 2. If replacements needed exceed k, shrink the window from the left
            # (Total Window Length - Most Frequent Letter Count > k)
            while (right - left + 1) - max(window_state.values()) > k:
                window_state[s[left]] -= 1
                left += 1

            # 3. Update our maximum length answer with the valid window size
            max_len = max(max_len, right - left + 1)

        return max_len


# Another soulution but NEETCODE VERS:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while (right - left + 1) - max(count.values()) > k: # values, get are built in
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res