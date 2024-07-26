# beats 84.49% of solutions

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution 1-----------------------------------------------------------------

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        res = ListNode(0, None)
        cur = res
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
            if list1 != None or list2 != None:
                cur.next = ListNode(0, None)
                cur = cur.next

        if list1 == None and list2 == None:
            return res
        if list1 == None:
            while list2 != None:
                cur.val = list2.val
                list2 = list2.next
                if list2 != None:
                    cur.next = ListNode(0, None)
                    cur = cur.next
        if list2 == None:
            while list1 != None:
                cur.val = list1.val
                list1 = list1.next
                if list1 != None:
                    cur.next = ListNode(0, None)
                    cur = cur.next
        return res



        