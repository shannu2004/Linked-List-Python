class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next
        
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        prev, curr = temp, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return temp.next

def create_linked_list(values):
    dummy=ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

head_values = [1, 2, 6, 3, 4, 5, 6]
val = 6

head = create_linked_list(head_values)

solution = Solution()
new_head = solution.removeElements(head, val)

result = linked_list_to_list(new_head)
print(result)


