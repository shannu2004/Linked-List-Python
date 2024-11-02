class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head:[ListNode]) -> [ListNode]:
        oddHead = ListNode(0)
        evenHead = ListNode(0)
        
        odd = oddHead
        even = evenHead
        isOdd = True
        
        while head:
            if isOdd:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            head = head.next
            isOdd = not isOdd
        
        even.next = None
        odd.next = evenHead.next
        
        return oddHead.next


def create_linked_list(lst):
    head = ListNode(0)
    current = head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return head.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


head = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
result_head = solution.oddEvenList(head)
result_list = linked_list_to_list(result_head)
print(result_list)  
