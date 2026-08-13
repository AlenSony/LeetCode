# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        length = 0
        arr = []
        while current != None:
            length += 1
            arr.append(current)
            current = current.next
        
        return arr[length // 2]

        