# beats 91.34% of solutions

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution 1 ----------------------------------------------------

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0, None)
        cur = res

        while l1 != None and l2 != None:
            if l1.val + l2.val + cur.val > 9:
                cur.next = ListNode(1, None)
                cur.val = l1.val + l2.val + cur.val - 10
            else:
                cur.next = ListNode(0, None)
                cur.val = l1.val + l2.val + cur.val
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        #now at least one of l1 and l2 is empty

        if l1 == None:
            while l2 != None:
                if l2.val + cur.val > 9:
                    cur.next = ListNode(1, None)
                    cur.val = l2.val + cur.val - 10
                else:
                    cur.next = ListNode(0, None)
                    cur.val = l2.val + cur.val
                l2 = l2.next
                cur = cur.next
        else:
            while l1 != None:
                if l1.val + cur.val > 9:
                    cur.next = ListNode(1, None)
                    cur.val = l1.val + cur.val - 10
                else:
                    cur.next = ListNode(0, None)
                    cur.val = l1.val + cur.val
                l1 = l1.next
                cur = cur.next
        
        #final check, remove last node
        temp = res
        if cur.val == 0:
            while temp.next != None and temp.next.next != None:
                temp = temp.next
            temp.next = None

        return res
                

# solution 2 ----------------------------------------------------
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        carry = 0
        
        while l1 is not None or l2 is not None:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            sum = num1 + num2 + carry
            carry = sum // 10
            sum = sum % 10
            res.append(sum)
            if l1 != None:
                l1 = l1.next 
            if l2 != None:
                l2 = l2.next

        if carry != 0:
            res.append(carry)

        SolutionHead = ListNode(0, None)
        tail = SolutionHead
        tail.val = res[0]
        
        for i in range(1, len(res)):
            tail.next = ListNode(res[i], None)
            tail = tail.next

        return SolutionHead



        


        


        