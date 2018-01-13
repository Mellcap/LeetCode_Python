# ----------------------------------
# Question Description
# ----------------------------------

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

------------------------------------
Examples:

Example 1:
---
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example2:
---
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

# ----------------------------------
# My Solution
# ----------------------------------

class Solution:
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        My solution's combinList method is too ugly. I don't know how to combine two lists effectively.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLength = len(nums1) + len(nums2)
        median1 = totalLength // 2
        median2 = median1 if totalLength % 2 else (median1 - 1)
        
        retList = self.combianList(nums1, nums2, lastIndex=median1)
        median = (retList[median2] + retList[median1]) / 2
        return median
        
    def combianList(self, nums1, nums2, lastIndex):
        retList = []
        i = 0
        num1 = nums1.pop(0)
        num2 = nums2.pop(0)
        while i <= lastIndex:
            i += 1
            if num1 <= num2:
                retList.append(num1)
                if not nums1:
                    retList.append(num2)
                    break
                num1 = nums1.pop(0)
            else:
                retList.append(num2)
                if not nums2:
                    retList.append(num1)
                    break
                nums2 = nums2.pop(0)

        if i < lastIndex:
            if not nums1:
                [retList.append(nums1.pop(0)) for x in range(lastIndex - i)]
            if not nums2:
                [retList.append(nums2.pop(0)) for x in range(lastIndex - i)]
                
        return retList

# Improved version
                

# ----------------------------------
# Instruction
# ----------------------------------

