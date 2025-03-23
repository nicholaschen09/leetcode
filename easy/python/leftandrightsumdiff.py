"""
You are given a 0-indexed integer array nums of size n.
Define two arrays leftSum and rightSum where:
leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
"""

class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        answer = [0] * n

        # Compute left sums
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        # Compute right sums
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        # Compute the answer array
        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i])

        return answer
            