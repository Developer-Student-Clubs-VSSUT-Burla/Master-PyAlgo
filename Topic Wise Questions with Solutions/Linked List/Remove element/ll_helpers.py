class ListNode:
    def __init__(self, x, n = None):
        """Definition for singly-linked list."""
        self.val = x
        self.next = n

def build_ll(arr):
    """Builds a linked list from array. Used for testing."""
    res = ListNode(None)
    pt = res

    for num in arr:
        pt.next = ListNode(num)
        pt = pt.next

    return res.next

def print_ll(head):
    """Prints a linked list in this format: x -> y -> z. Used for testing."""
    res = []

    while None != head:
        res.append(str(head.val))
        head = head.next

    print(' -> '.join(res))