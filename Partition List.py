class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head:[ListNode], x: int) ->[ListNode]:
        d1 = ListNode(0)
        front = d1
        d2 = ListNode(0)
        back = d2
        
        while head:
            if head.val < x:
                front.next = head
                front = front.next
            else:
                back.next = head
                back = back.next
            head = head.next
        
        back.next = None
        front.next = d2.next
        return d1.next

def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = create_linked_list([1, 4, 3, 2, 5, 2])
x = 3
solution = Solution()
new_head = solution.partition(head, x)
output = linked_list_to_list(new_head)
print(output)  
