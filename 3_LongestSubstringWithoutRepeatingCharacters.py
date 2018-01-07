# ----------------------------------
# Question Description
# ----------------------------------

'''

Given a string, find the length of the longest substring without repeating characters.

------------------------------------
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# ----------------------------------
# My Solution
# ----------------------------------

class Solution:
    '''
    My solution cause the RecursionError: maximum recursion depth exceeded while calling a Python object.
    '''
    
    def __init__(self):
        self.maxLength = 0
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.findSubString(s)
        return self.maxLength
        
        
    def findSubString(self, targetString):
        newLength = 0
        subCache = {}
        for i, item in enumerate(targetString):
            if item not in subCache:
                subCache[item] = i
                newLength += 1
            else:
                if newLength > self.maxLength:
                    self.maxLength = newLength
                startPoint = subCache[item] + 1
                return self.findSubString(targetString[startPoint:])


# Improved version
class Solution:
    
    def __init__(self):
        self.maxLength = 0
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.findSubString(s)
        return self.maxLength
        
        
    def findSubString(self, targetString):
        newLength = 0
        subCache = {}
        startPoint = 0
        for i, item in enumerate(targetString):
            if item not in subCache:
                subCache[item] = i
                newLength += 1
            else:
                # change the newLength and replace the index of the repeat item.
                cachedIndex = subCache[item]
                newLength = i - cachedIndex
                subCache[item] = i
                # delete the former records
                for x in range(startPoint, cachedIndex):
                    del[subCache[targetString[x]]]
                # change the startPoint
                startPoint = cachedIndex + 1

            # replace the maxLength is needed                 
            if newLength > self.maxLength:
                self.maxLength = newLength  
                
                

        
        


# ----------------------------------
# Instruction
# ----------------------------------


