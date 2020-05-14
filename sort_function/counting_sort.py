# 计数排序
# 适合的场景：非负数，整数，值种类不多的情况合适
# 负数的时候可以给每个值加一个正整数使其变为正数
# 有小数点的时候可以给其乘以10的倍数，使其变为整数

def countingSort(li):
    """
    计数排序
    :param li:
    :return:
    """
    n = len(li)
    if n <= 1:
        return
    # 找到最大值区间
    max = li[0]
    for i in range(1, n):
        if li[i] > max:
            max = li[i]
    # 创建类似桶的数组,下标范围是0-max;
    c = [0] * (max + 1)
    # 遍历li，把每个值对应的个数存入桶中
    for i in range(n):
        c[li[i]] += 1
    # 遍历桶数组，依次累加个数，使当前下标对应的值为比此下标小的数字的总数 # 好乱啊
    for i in range(1, max + 1):
        c[i] = c[i - 1] + c[i]
    # 创建一个新数组，遍历li，把桶中对应的元素取出来放到新数组中
    newLi = [''] * n
    i = n - 1
    # 这里倒着取是为了保证稳定性，i在这里是递减的，后面有相同数字的时候会排到较前面的位置。所以从后往前取li元素，
    # 能保证取出来还排到较后面的位置
    while i >= 0:
        newLi[c[li[i]] - 1] = li[i]
        c[li[i]] -= 1
        i -= 1
    for i in range(n):
        li[i] = newLi[i]


if __name__ == '__main__':
    li = [3, 3, 3, 6, 1, 7, 2, 3, 6, 8, 1, 3, 7, 9, 11, 16, 12, 12, 14, 16, 21, 2, 5, 6, 1, 7, 11, 26, 9]
    print(len(li))
    countingSort(li)
    print(li)
    print(len(li))
