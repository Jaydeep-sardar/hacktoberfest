from ds import ListNode

def palindromic_linked_list(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Find the middle (slow will be at mid)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second_half = prev

    # Step 3: Compare first half and reversed second half
    p1, p2 = head, second_half
    while p2:  # only need to check second half
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next

    return True
