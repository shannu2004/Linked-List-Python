class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        current = head.next
        dummy = ListNode()
        result = dummy
        sum_between_zeros = 0
        
        while current:
            if current.val == 0:
                if sum_between_zeros > 0:
                    result.next = ListNode(sum_between_zeros)
                    result = result.next
                sum_between_zeros = 0
            else:
                sum_between_zeros += current.val
            current = current.next
        
        return dummy.next

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])

sol = Solution()
result = sol.mergeNodes(head)

print_linked_list(result)
