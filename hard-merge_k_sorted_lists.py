# beats

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


#solution 1------------------------------------------------------------------------ this works but exceeds the time limit

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListHead = ListNode()
        cur = ListHead
        list_status = []
        if len(lists) == 0:
            return ListHead.next
        for i in range(len(lists)):
            if lists[i] == None:
                list_status.append(0)
            else:
                list_status.append(1)  # non empty
        
        while 1 in list_status:
            number_tracker = []
            index_tracker = []
            for i in range(len(lists)):
                if list_status[i] == 0:
                    continue
                number_tracker.append(lists[i].val)
                index_tracker.append(i)
            low = min(number_tracker)
            index = index_tracker[number_tracker.index(low)]
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] == None:
                list_status[index] = 0
        
        return ListHead.next
             

#solution 2------------------------------------------------------------------------ 
        