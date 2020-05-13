# 冒泡排序

def bubble_sort(li):
    n = len(li)
    if n <= 1:
        return None
    flag = False
    for i in range(n):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j],li[j+1] = li[j + 1],li[j]
                flag = True
        if not flag:
            break

def bubble_sort_test():
    li = [6, 82, 89, 23, 2, 98, 0, 2, 56, 8, 2, 1, 6, 9, 54345, 923, 0, 23, 7, 456, 57, 908, 232]
    bubble_sort(li)
    assert li == [0, 0, 1, 2, 2, 2, 6, 6, 7, 8, 9, 23, 23, 56, 57, 82, 89, 98, 232, 456, 908, 923, 54345]

if __name__ == '__main__':
    bubble_sort_test()