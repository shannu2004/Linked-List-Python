from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head:[ListNode]) ->[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def create_linked_list(values: List[int]) -> [ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head:[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

solution = Solution()
middle_node = solution.middleNode(head)


result = linked_list_to_list(middle_node)

print("Output:", result)  
