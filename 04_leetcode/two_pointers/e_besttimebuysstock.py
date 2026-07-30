"""
Problem: You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Difficulty: [Easy]
Pattern: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    maxP = max(maxP, profit) 
            else:
                l = r
            r += 1
        return maxP


"""
OTHER SOLUTION for loop does the incremental:

In Python, a for loop using range(len(prices)) automatically handles the incrementing under the hood for you behind the scenes.
Every single time the loop finishes one round, Python automatically steps right up to the next index (0, then 1, then 2, and so on) until it reaches the end of the list.

while loop: manually pressing the gas pedal (r += 1), so if forgotten it, the car stops (or loops forever).

for loop: on automatic cruise control; Python handles stepping right forward automatically on every pass.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1. Initialize our pointers and tracker:
        #    - 'left' acts as our buy day (starts at index 0)
        #    - 'maxp' tracks our record-high profit (starts at 0)
        left = 0
        maxp = 0

        # 2. Walk through every day using 'right' as our selling/scanning day
        for right in range(len(prices)):

            # 3. If the current price is lower than our buy price,
            #    we found a cheaper day to buy! Move our 'left' pointer here.
            if prices[right] < prices[left]:
                left = right

            # 4. Otherwise, calculate the profit if we sold today
            #    and update our max profit if it beats our record.
            else:
                curr_profit = prices[right] - prices[left]
                maxp = max(maxp, curr_profit)

        # 5. Return the highest profit we found across the entire array
        return maxp