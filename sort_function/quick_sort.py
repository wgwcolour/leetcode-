# 快速排序
# 快速排序也可以做到原地排序，但不具有稳定性

def quick_sort_main(li):
    n = len(li)
    l = 0
    r = n - 1
    quick_sort(li, l, r)


def quick_sort(li, l, r):
    # 递归的中止条件
    if l >= r:
        return
    # 需要先获取本次排序的中点位置
    mid = partition(li, l, r)
    quick_sort(li, l, mid - 1)
    quick_sort(li, mid + 1, r)


def partition(li, l, r):
    # 原地移动 位置互换，最终结果是比p小的点在左边，比p大的点在右面，返回p位置
    p = li[r]
    i, j = l, l
    while j < r:
        if li[j] < p:
            li[i], li[j] = li[j], li[i]
            i += 1
        j += 1
    li[i], li[r] = li[r], li[i]  # 把p点和大于p的集合的第一个点互换位置，这样p就在中间了。
    return i


if __name__ == '__main__':
    li = [6, 82, 89, 23, 2, 98, 0, 2, 56, 8, 2, 1, 6, 9, 54345, 923, 0, 23, 7, 456, 57, 908, 232]
    quick_sort_main(li)
    print(li)
