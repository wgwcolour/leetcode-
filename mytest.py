# 用作测试，leetcode调试实在太不方便了
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def genList(li):
    node = ListNode(0)
    count = 0
    head = None
    for i in li:
        node.next = ListNode(i)
        if count == 0:
            head = node
        count += 1
        node = node.next
    return head.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head:
            # 重新创建一个新的head
            tmp = ListNode(head.val)
            tmp.next = head.next
            head.next = node
            node = head
            head = tmp.next
        return node
if __name__ == '__main__':
    Solution().reverseList(genList([1,2,3,4,5]))