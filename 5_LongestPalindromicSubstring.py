# ----------------------------------
# Question Description
# ----------------------------------

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

------------------------------------
Examples:

Example 1:
---
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer. 

Example:
---
Input: "cbbd"
Output: "bb"

***
Manacher's Algorithm
http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
'''


# ----------------------------------
# Instruction
# ----------------------------------

class Solution:
    
    def preProcess(self, s):
        """
        Transform s into T
        For example, s = 'abba', T = '^#a#b#a#a#$'
        ^ and $ signs are sentinels appended to each end to avoid bounds checking.
        """
        if len(s) == 0:
            return '^$'
        ret = '^'
        for i in s:
            ret += '#%s' % i
        ret += '#$'
        return ret
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = self.preProcess(s)
        n = len(T)
        P = [0] * n
        Center, Right = 0, 0
        
        for i in range(1, n - 1):
            i_mirror = 2 * Center - i  # equals to i' = C - (i - C)
            
            P[i] = min(Right - i, P[i_mirror]) if (Right > i) else 0
            
            # Attemp to expand palindrome centered at i
            while (T[i + 1 + P[i]] == T[i - 1 - P[i]]):
                P[i] += 1

            # If palindrom centered at i expand past R,
            # adjust center based on expanded palindrome.
            if (i + P[i] > Right):
                Center = i
                Right = i + P[i]
            
        # Find the maximum element in P
        maxLen = 0
        centerIndex = 0
        for i in range(1, n - 1):
            if P[i] > P[centerIndex]:
                maxLen = P[i]
                centerIndex = i
        
        start = (centerIndex - 1 - maxLen) // 2
        return s[start: start + maxLen]
            
        


