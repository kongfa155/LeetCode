# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        cur = result
        c = 0
        i = l1
        j = l2
        while i or j or c:
            val1 = i.val if i else 0
            val2 = j.val if j else 0
            total = c + val1 + val2
            c = total // 10 
            cur.next = ListNode(total % 10)
            cur = cur.next
            if i:
                i = i.next
            if j:
                j = j.next
        return result.next
        