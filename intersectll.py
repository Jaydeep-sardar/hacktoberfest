from ds import ListNode

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    p1, p2 = headA, headB
    
    # Loop until both pointers meet (either at intersection or at None)
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    
    return p1  # Could be intersection node or None
