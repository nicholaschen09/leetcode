# Given a string s, find the length of the longest substring without duplicate characters.
#  
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#  
# Constraints:
# 
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            # If the character is already in the dictionary and its last index is within the current window
            if char in last_index and last_index[char] >= start:
                start = last_index[char] + 1
            last_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length
            