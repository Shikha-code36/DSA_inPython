'''
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list
'''


# Approach 1 - count



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0

        current = head
        
        while current:
            count+=1
            current = current.next

        current = head

        index = count//2

        while current and index>0:
            current = current.next
            index-=1
        
        return current

# T:O(N + N/2)
# S:O(1)

# Approach 2
    



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
# T:O(N)
# S:O(1)
