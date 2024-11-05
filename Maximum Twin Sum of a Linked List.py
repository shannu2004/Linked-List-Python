class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        n = len(stack)
        return max(stack[i] + stack[-(i+1)] for i in range(n >> 1))

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

head = create_linked_list([5, 4, 2, 1])

solution = Solution()
result = solution.pairSum(head)
print("Max Pair Sum:", result)
