def linked_list_reversal(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    new_head = linked_list_reversal(head.next)
    head.next.next = head
    head.next = None
    return new_head
