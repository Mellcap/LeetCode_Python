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
                
class Solution:
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        The core is to find the (K+1)th num.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 == 1:
            k = totalLength // 2
            return self.findKth(nums1, nums2, k)
        else:
            k1 = totalLength // 2
            k2 = k1 - 1
            return (self.findKth(nums1, nums2, k1) + self.findKth(nums1, nums2, k2)) / 2
        
    def findKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)

        if m > n:  # make sure the first array smaller
            return self.findKth(nums2, nums1, k)
        
        left, right = -1, m                                        # [-1, m) => include the left one, exclude the right one.
        while left < right - 1:                                    # right - 1 == m - 1, which is the last index
            mid = left + (right - left) // 2
            kNext = k - mid
            if 0 <= kNext < n and nums1[mid] > nums2[kNext]:       # mid not meet the condition, so exclude mid
                right = mid
            else:                                                  # mid meet the condition, so include mid
                left = mid
            
        k1 = nums1[left] if left >= 0 else float('-inf')
        k2 = nums2[k - left - 1] if (k - left - 1) >= 0 else float('-inf')
        
        return max(k1, k2)


# ----------------------------------
# Instruction
# ----------------------------------

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1: 
            return self.getKth(nums1, nums2, (len1 + len2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2)/2) + \
                    self.getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m    
        while left < right:
            mid = left + (right - left) / 2
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)



