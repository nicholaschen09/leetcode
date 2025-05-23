# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# 
# Return the answer in an array.
#  
# Example 1:
# 
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
# 
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
# 
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
#  
# Constraints:
# 
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  # Sort nums to determine ranking
        num_map = {}  # Dictionary to store the count of smaller numbers
        
        # Assign each number its rank (first occurrence only)
        for i, num in enumerate(sorted_nums):
            if num not in num_map:  # Only store the first occurrence
                num_map[num] = i  
        
        # Map back to the original array
        return [num_map[num] for num in nums]
