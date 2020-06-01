"""
    汉诺塔问题：
        设有三根标号为A,B,C的柱子上，在A柱上放着n个盘子，每一个都比下面的略小一点，要求把A柱上的盘子全部移动到C柱上，
        规则是：一次只能移动一个盘子；移动的过程中大盘只能放在小盘下面；在移动过程中盘子可以放在A,B,C的任意一个柱子上。
    递归三步曲：
        1.找终止条件，C以外的圆柱上只有一个盘子
        2.找返回值，
        3.本级递归应该做什么

    递归过程：
    参考网址：https://blog.csdn.net/qq_37873310/article/details/80461767
"""


def move(i, m, n):
    global k
    k += 1
    print('第{}次移动：把{}号圆盘从{}移到{}'.format(k, i, m, n))


def hanoi(n, A, B, C):
    if n == 1:  # 步1
        move(1, A, C)
    else:
        hanoi(n-1, A, C, B)
        move(n, A, C)
        hanoi(n-1, B, A, C)


if __name__ == '__main__':
    k = 0
    hanoi(3, 'A', 'B', 'C')
