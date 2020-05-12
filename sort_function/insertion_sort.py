# 插入排序

def insertion_sort(li):
    n = len(li)
    if n <= 1:
        return None
    for i in range(1,n):
        value = li[i]
        j = i-1
        while j >= 0:
            if li[j] > value:
                li[j + 1] = li[j]
            else:
                break
            j -= 1
        li[j + 1] = value

def insertion_sort_test():
    li = [1,3,54,73,3,790,3,12,65,7,9,2,4,9]
    insertion_sort(li)
    assert li == [1, 2, 3, 3, 3, 4, 7, 9, 9, 12, 54, 65, 73, 790]

if __name__ == '__main__':
    insertion_sort_test()