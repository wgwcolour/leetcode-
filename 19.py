class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 参考题解 使用双指针，先移动指针a，使a与b间隔n，然后一起移动到a=None时，b的下一个结点即为要删除的倒数第n个结点
# 使用哨兵，处理边界问题，防止只给了 [一个结点] 的情况
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