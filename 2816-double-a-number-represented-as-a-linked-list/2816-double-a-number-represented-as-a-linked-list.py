# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        a = ""
        while curr:
            a+= str(curr.val)
            curr = curr.next 
        a = str(int(a)*2)
        d = ListNode(None)
        temp = d 
        sys.set_int_max_str_digits(100000)        
        for i in a:
            t = ListNode(i)
            temp.next = t
            temp = t
        return d.next 
