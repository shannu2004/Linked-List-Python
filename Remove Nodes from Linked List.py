class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head:[ListNode]) ->[ListNode]:
        stack = []
        dummy = headNew = ListNode(None, head)
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        for node in stack:
            headNew.next = node
            headNew = headNew.next
        headNew.next = None  
        return dummy.next

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

head = list_to_linkedlist([5, 2, 13, 3, 8])
solution = Solution()
result_head = solution.removeNodes(head)
result_list = linkedlist_to_list(result_head)
print(result_list)




