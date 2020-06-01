"""
    折半查找（二分查找）问题：
        前提：数组中的元素必须是有序的
        将被查找的数组分为三部分，依次是中值前、中值、中值后，将指定元素和数组的中值进行比较，
        如果指定元素小于中值则在（中值前）中找，
        如果指定元素大于中值则在（中值后）中找，
        如果指定元素等于中值则直接返回。
        依次查找后，如果不包含指定元素，则返回-1；

    递归三步曲：
        1.找终止条件，查找到值或数组不可再分
        2.找返回值，值索引或-1
        3.本级递归应该做什么，判断待查找值和中值关系，进行相应的查找操作

    递归过程：
"""
import math


def halfIntervalSearch(items, start, end, key):
    if start <= end:
        mid = start + math.ceil((end - start) / 2)
        if items[mid] is key:
            return mid
        elif items[mid] > key:
            return halfIntervalSearch(items, start, mid - 1, key)
        else:
            return halfIntervalSearch(items, mid + 1, end, key)
    else:
        return -1


if __name__ == '__main__':
    items = [1, 1, 2, 3, 5, 6, 9, 12]
    print(halfIntervalSearch(items, 0, len(items)-1, 2))
