# ----------------------------------
# Question Description
# ----------------------------------

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

------------------------------------
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# ----------------------------------
# My Solution
# ----------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.node2num(l1)
        num2 = self.node2num(l2)
        num = num1 + num2
        return self.num2node(num)
        
    def node2num(self, node):
        if not node.next:
            return node.val
        return node.val + 10 * self.node2num(node.next)
    
    def num2node(self, num):
        node = ListNode(num % 10)
        val = num // 10
        if not val:
            return node
        node.next = self.num2node(val)
        return node



# ----------------------------------
# Instruction
# ----------------------------------

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            
        # the sum of last two nodes > 10
        if carry:
            current.next = ListNode(1)
            
        return dummy.next
