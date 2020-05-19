# 二分查找
def bsearch(li, item):
    n = len(li)
    l = 0
    r = n - 1
    while l <= r:
        mid = (r + l) // 2
        if li[mid] == item:
            return mid
        elif li[mid] > item:
            r = mid - 1
        else:
            l = mid + 1
    return None


# 二分查找变形
# 前提：给定列表内有相同元素
# 1.查找第一个值等于给定值的元素
def bsearch_1(li, item):
    n = len(li)
    l = 0
    r = n - 1
    flag = None  # 当有相同值的时候，先标记一下位置
    while l <= r:
        mid = (r + l) // 2
        if li[mid] > item:
            r = mid - 1
        elif li[mid] == item:
            flag = mid  # 标记位置，然后查看此位置前面是否还有同样的值
            while mid > 0 and li[mid] == item:
                if li[mid - 1] == item:
                    flag = mid - 1
                mid -= 1
            return flag
        else:
            l = mid + 1
    return flag


if __name__ == '__main__':
    li = [1, 4, 5, 6, 8, 8, 9, 11, 45, 76, 79]
    # li = [1,4,5,8,8,45,76,79]
    print(bsearch_1(li, 8))
