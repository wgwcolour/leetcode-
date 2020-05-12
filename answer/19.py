# 删除链表倒数第n个结点
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 参考题解 使用双指针，先移动指针a，使a与b间隔n，然后一起移动到a=None时，b的下一个结点即为要删除的倒数第n个结点
# 使用哨兵，处理边界问题，防止只给了 [一个结点] 的情况
# 这个思路用在找倒数第n个的时候真棒！
class Solution:
    # a = [0,1,2,3,4,5,None]
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 遍历一次
        # 哨兵结点放到最前面
        sentry = ListNode(0)
        sentry.next = head
        p = head
        q = sentry
        for i in range(n):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return sentry.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 遍历两次
        def lens(head):

            count = 0
            while head:
                head = head.next
                count += 1
            return count

        count = 0
        le = lens(head)
        node = head
        if n == 1 and le != 1:

            while count < le - 1 -1:
                node = node.next
            node.next = None
        elif n == 1:
            head = None
        elif le == n:
            head = head.next
        else:
            while count < le - n - 1:
                node = node.next
                count += 1
            node.next = node.next.next
        return head

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

if __name__ == '__main__':
    li = [1,2]
    head = genList(li)
    a = Solution().removeNthFromEnd(head,1)
    print(1)