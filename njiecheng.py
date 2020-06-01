"""
    n阶乘问题
        1！=1
        2！= 2*1 = 2*1!
        3！= 3*2*1 = 3*2!
        ...
        (n-1)! = (n-1)*(n-2)...2*1 = (n-1)*(n-2)!
        n! = n*(n-1)*(n-2)...2*1 =  n*(n-1)!

    递归三步曲：
        1.找终止条件，当n为1终止
        2.找返回值，当前阶乘结果
        3.本级递归应该做什么，本级数乘以上级阶乘

    递归过程：
    n = 5
    5 * nFactorial(4)                       # 递进
    5 * (4 * nFactorial(3))                 # 递进
    5 * (4 * (3 * nFactorial(2)))           # 递进
    5 * (4 * (3 * (2 * nFactorial(1))))     #达到终止条件n=1，而nFactorial(1) = 1
    5 * (4 * (3 * (2 * 1)))                 # 归来
    5 * (4 * (3 * 2)))                      # 归来
    5 * (4 * 6))                            # 归来
    5 * (24)                                # 归来
    120                                     # 归来
"""


def nFactorial(n):
    if n > 1:  # 步1
        return n * nFactorial(n - 1)  # 步2 步3
    return 1


if __name__ == '__main__':
    print(nFactorial(int(input('Enter num:'))))
