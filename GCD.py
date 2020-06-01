"""
    最大公约数（欧几里得）问题
        数学上的定义：定义g是整数a和b的最大公约数，当且仅当g是同时整除a和b的数中最大值。
        条件为：a>b
        gcd(a,b)={
                    a,             if b=0
                    gcd(b,a mod b),if b≠0
                 }

    递归三步曲：
        1.找终止条件，当b为0终止
        2.找返回值，当前a值
        3.本级递归应该做什么，a = b(将a赋值给b), b = a%b(b为a与b的余数)

    递归过程：
    a = 12 , b = 8
    GCD(8, 12 % 8)                          # 递进
    GCD(4, 8 % 4)                           # 递进
    a = 4                                        #达到终止条件b=0，而此时a=4
    return a                                 # 归来
    return a                                # 归来
    4
"""


def GCD(a, b):
    if b == 0:  # 步1
        return a
    return GCD(b, a % b)    # 步2 步3


if __name__ == '__main__':
    print(GCD(12, 8))
