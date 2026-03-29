class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid = count // 2
        temp = head
        for _ in range(mid - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
