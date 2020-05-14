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


def exercise(li, k):
    """
    练习题：找到数组li中的第k大的元素
    例如li=[3,6,1,2,8],k=3,返回值为3
    :param li:
    :param k:
    :return:
    """

    def get_k(li, l, r, k):
        mid = partition(li, l, r)
        # [1,2,3,4,5,6]
        if k == len(li) - mid: # mid的位置正好是第k大
            return li[mid]
        elif len(li) - k > mid: # 第mid大的元素大于第k大，k在右边的数组中
            return get_k(li, mid + 1, r, k)
        else: # k在左边的数组中
            return get_k(li, l, mid - 1, k)

    n = len(li)
    l = 0
    r = n - 1
    i = get_k(li, l, r, k)
    print(i)


if __name__ == '__main__':
    li = [6, 82, 89, 23, 2, 98, 0, 2, 56, 8, 2, 1, 6, 9, 54345, 923, 0, 23, 7, 456, 57, 908, 232]
    quick_sort_main(li)
    print(li)
    exercise(li, 2)
