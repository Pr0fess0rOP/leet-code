# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next      

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Just to initialize
        dummy = ListNode()

        # We return res, not dummy
        res = dummy

        total = carry = 0

        while l1 or l2 or carry: # check if all stuff are empty or not
            # Total is the unrestricted result of a single digit place.
            total = carry

            if l1: # if l1 has value in it
                total += l1.val
                l1 = l1.next
            if l2: # if l2 has value in it
                total += l2.val
                l2 = l2.next

            # Digit at current place
            num = total % 10 # get the remainder when divided by 10.

            # Digit additions for next place
            carry = total // 10 # get the floor division

            # Assign our num to dummy.next node instead of None
            dummy.next = ListNode(num)
            # Get that dummy.next as our dummy.val with next as None
            dummy = dummy.next

        return res.next