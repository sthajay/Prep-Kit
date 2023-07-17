# 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

        # obj = dict()
        # curr = head
        # while curr:
        #     if curr in obj:
        #         return True
        #     obj[curr] = 1
        #     curr = curr.next

        # return False

        # obj = set()
        # curr = head
        # while curr:
        #     if curr in obj:
        #         return True
        #     obj.add(curr)
        #     curr = curr.next

        # return False
