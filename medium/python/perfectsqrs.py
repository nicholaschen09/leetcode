# Given an integer n, return the least number of perfect square numbers that sum to n.
# 
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
#  
# Example 1:
# 
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#  
# Constraints:
# 
# 1 <= n <= 10^4

class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] will be least number of perfect squares tht sum to i.
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # loop 
        for i in range(1, n + 1):
            j = 1
            # when perfect square of j <= i
            while j * j <= i:
                # find the minimum of the current and one with another perfect square added to it
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                # increment j
                j += 1
                
        return dp[n]
