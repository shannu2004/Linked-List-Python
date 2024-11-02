class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head:[ListNode], k: int) ->[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        curr.next = head
        k %= length
        rotate = length - k
        
        while rotate:
            curr = curr.next
            rotate -= 1
        
        head = curr.next
        curr.next = None
        
        return head

def create_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

head = create_linked_list([1, 2, 3, 4, 5])
k = 2
solution = Solution()
rotated_head = solution.rotateRight(head, k)
print(linked_list_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]
