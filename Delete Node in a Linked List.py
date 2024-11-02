class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        # Copy the value from the next node to the current node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next

def print_linked_list(head):
    """Helper function to print the linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


head = create_linked_list([4, 5, 1, 9])
node_to_delete = head.next  


print("Original linked list:")
print_linked_list(head)


solution = Solution()
solution.deleteNode(node_to_delete)


print("Linked list after deleting node 5:")
print_linked_list(head)
