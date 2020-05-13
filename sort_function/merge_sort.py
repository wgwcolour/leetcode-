# 归并排序
# 分治的思想是分而治之，把一个数组分成两个，排好序以后再合起来。而数组元素太多的时候，就要用到递归
# 归并排序是可以实现原地排序的
def merge_sort_main(li):
    n = len(li)
    merge_sort(li, 0, n - 1)


def merge_sort(li, l, r):
    """
    归并排序，实现原地排序
    :param li:要排序的数组
    :param l: 要排序的下标起始位置
    :param r: 要排序的下标终点位置
    :return:
    """
    # 递归的终止条件
    if l >= r:
        return
    # 中间数
    mid = (l + r) // 2
    merge_sort(li, l, mid)
    merge_sort(li, mid + 1, r)
    merge(li, l, mid, r)


def merge(li, l, mid, r):
    # 创建两个临时数组用来存左侧和右侧的数据
    n1 = mid - l + 1
    n2 = r - mid
    L = [0] * n1
    R = [0] * n2
    # 把li中的相应的位置的数据拷贝出来
    for i in range(n1):
        L[i] = li[l + i]
    for i in range(n2):
        R[i] = li[mid + 1 + i]
    # 把拷出来的两个数组，原地排序到li中
    q, p = 0, 0
    while q < n1 and p < n2:
        if L[q] > R[p]:
            li[l] = R[p]
            p += 1
        else:
            li[l] = L[q]
            q += 1
        l += 1
    # 如果有剩余未排入到li的部分，将其顺序插入li
    while q < n1:
        li[l] = L[q]
        l += 1
        q += 1
    while p < n2:
        li[l] = R[p]
        l += 1
        p += 1


if __name__ == '__main__':
    li = [6, 82, 89, 23, 2, 98, 0, 2, 56, 8, 2, 1, 6, 9, 54345, 923, 0, 23, 7, 456, 57, 908, 232]
    # li = [611, 82]
    merge_sort_main(li)
    print(li)
