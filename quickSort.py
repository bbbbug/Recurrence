"""
    快速排序问题：
        快速排序是冒泡排序的改进版，也是最好的一种内排序。
        思想: 1.在待排序的元素任取一个元素作为基准(通常选第一个元素，但最的选择方法是从待排序元素中随机选取一个作为基准)，称为基准元素；
             2.将待排序的元素进行分区，比基准元素大的元素放在它的右边，比其小的放在它的左边；
             3.对左右两个分区重复以上步骤直到所有元素都是有序的。
             所以可以把快速排序联想成东拆西补或西拆东补，一边拆一边补，直到所有元素达到有序状态。
"""


def swap(items, start, end):
    '''
    :param items:待排序序列
    :param start:序列排序起始位置
    :param end:序列排序终止位置
    :return:返回这一次排序的基准位置，一般选择序列第一个作为基准值
    排序过程：
        5, 1, 3, 8, 9, 12, 5, 7
        ↑

    '''
    key = items[start]
    while start < end:
        while start < end and items[end] > key:
            end -= 1
        items[start] = items[end]
        while start < end and items[start] <= key:
            start += 1
        items[end] = items[start]
    items[start] = key
    return start


"""
    递归三步曲：
        1.找终止条件，start == end
        2.找返回值，
        3.本级递归应该做什么，交换使分区元素有序

    递归过程：
"""


def quickSort(items, start, end):
    if start < end:
        par = swap(items, start, end)
        if par - 1 > start:
            quickSort(items, start, par - 1)
        if par + 1 < end:
            quickSort(items, par + 1, end)
    return items


if __name__ == '__main__':
    items = [5, 1, 3, 8, 9, 12, 5, 7]
    print(quickSort(items, 0, len(items) - 1))
