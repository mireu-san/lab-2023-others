# Correct answer. But tried other way.
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         while temp and temp.next:
#             head = head.next
#             temp = temp.next.next

#         return head

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head # initialise both pointers at head of list
        
        # iterate as long as fast pointer and its next node are none.
        while fast and fast.next:
            slow = slow.next # moved falow pointer 1 step
            fast = fast.next.next # Moved fast pointer 2 steps

        # when loop ends, slow pointer will be at middle.
        # if there are 2 middle nodes, then slow pointer will be at second middle node.
        return slow

# Explained:
# Both pointers start at the head of the list.
# In each iteration of the loop, the slow pointer moves one step, and the fast pointer moves two steps.
# If the list has an odd number of nodes, the fast pointer will become None, and the slow pointer will be at the middle node.
# If the list has an even number of nodes, the fast pointer's next will become None, and the slow pointer will be at the second middle node.