# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Chia danh sách liên kết thành hai nửa
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None

        # Đệ quy sắp xếp từng nửa
        left = self.sortList(left)
        right = self.sortList(right)

        # Hợp nhất hai danh sách đã sắp xếp
        return self.merge(left, right)

    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Nối phần còn lại của danh sách
        if left:
            current.next = left
        elif right:
            current.next = right

        return dummy.next