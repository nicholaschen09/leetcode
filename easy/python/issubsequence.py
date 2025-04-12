# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# 
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#  
# Example 1:
# 
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# 
# Input: s = "axc", t = "ahbgdc"
# Output: false
#  
# Constraints:
# 
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0 # creates pointers 
        while i < len(s) and j < len(t): 
                if s[i] == t[j]: # check if the letters match 
                    i += 1 # this is priority so if this matches move next pointer
                j += 1 # else move this pointer since the letter is prolly a random one
        return i == len(s) # if the pointer reaches end of the string s then the count will eqaul to len(s) and return true else false