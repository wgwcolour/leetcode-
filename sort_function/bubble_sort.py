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
    li = [1,3,54,73,3,790,3,12,65,7,9,2,4,9]
    bubble_sort(li)
    assert li == [1, 2, 3, 3, 3, 4, 7, 9, 9, 12, 54, 65, 73, 790]

if __name__ == '__main__':
    bubble_sort_test()