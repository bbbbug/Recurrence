"""
    归并排序问题：
        1.当我们要排序这样一个数组的时候，归并排序法首先将这个数组分成一半
        2.然后想办法把左边的数组给排序，右边的数组给排序，之后呢再将它们归并起来。
        3.当我们对左边的数组和右边的素组进行排序的时候，再分别将左边的数组和右边的数组分成一半，然后对每一个部分先排序，再归并。
        4.对于上面的每一个部分呢，我们依然是先将他们分半，再归并，
        5.分到一定细度的时候，每一个部分就只有一个元素了，那么我们此时不用排序，对他们进行一次简单的归并就好了。
        6.归并到上一个层级之后继续归并，归并到更高的层级，
        7.直到归并完成
    递归三步曲：
        1.找终止条件，分到只有一个元素
        2.找返回值，返回合并完的序列
        3.本级递归应该做什么，将递归的序列，拿去合并

    递归过程：
"""


def sort(Aitems, Bitems):
    items = []
    a = len(Aitems)
    b = len(Bitems)
    i = j = 0
    while i < a and j < b:
        if Aitems[i] <= Bitems[j]:
            items.append(Aitems[i])
            i += 1
        else:
            items.append(Bitems[j])
            j += 1
    if i < a:
        items += Aitems[i:]
    else:
        items += Bitems[j:]
    return items


def MergeSort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    MergeSort(items[:mid])
    MergeSort(items[mid:])
    return sort(MergeSort(items[:mid]), MergeSort(items[mid:]))


if __name__ == '__main__':
    items = [2, 1, 10, 5, 8, 9, 2, 3, 7]
    print(MergeSort(items))
