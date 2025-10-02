from ds import ListNode

def linked_list_loop(head: ListNode) -> bool:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # cycle detected
            return True
    
    return False  # no cycle
