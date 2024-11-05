import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head:[ListNode]) -> [ListNode]:
        temp1 = head
        temp2 = head.next
        while temp2:
            temp = ListNode(math.gcd(temp1.val, temp2.val))
            temp.next = temp2
            temp1.next = temp
            temp1 = temp2
            temp2 = temp2.next
        return head

def list_to_linkedlist(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = list_to_linkedlist([18, 6, 10, 3])
solution = Solution()
result_head = solution.insertGreatestCommonDivisors(head)
result_list = linkedlist_to_list(result_head)
print(result_list)
