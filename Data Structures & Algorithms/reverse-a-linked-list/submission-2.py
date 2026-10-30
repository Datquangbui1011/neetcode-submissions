# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # To check my understanding about problem, I have reverse the link list and return with a new head
        # So to start I will reverse pointer in place, each node one at the time. So I will start with prev which as null, and curr is our head
        prev = None
        curr = head
        # While we check the curr is not null!
        while curr:
            #firstly I will save the next node, to don't make lost the rest of the list
            next = curr.next
            #Then I point the curr.next back to prev, this should be the revese step
            curr.next = prev
            #Then I move both pointer one step forward
            prev = curr
            curr = next
        return prev
