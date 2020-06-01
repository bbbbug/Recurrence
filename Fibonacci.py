"""
    斐波那契数列问题：
        斐波那契数列（Fibonacci sequence），又称黄金分割数列，
        因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”。
        波那契数列以递归的形式进行定义：
            F0= 1 F1 =1 Fn = Fn−1 + Fn−2
    递归三步曲：
        1.找终止条件，n <= 1
        2.找返回值，当前Fk的值
        3.本级递归应该做什么，Fk = Fk-1 +Fk-2

    递归过程：
    n = 5
    Fibonacci(5-1) + Fibonacci(5-2)                          # 递进
    Fibonacci(4-1) + Fibonacci(4-2) + Fibonacci(3-1) + Fibonacci(3-2)                           # 递进
    Fibonacci(3-1) + Fibonacci(3-2) + Fibonacci(2-1) + Fibonacci(2-2) + Fibonacci(2-1) + Fibonacci(2-2) + Fibonacci(1)  # 有1个达到终止条件开始返回
    Fibonacci(3-1) + 6      # 有6个达到终止条件
    Fibonacci(1) + Fibonacci(1) + 6                                   #有8个达到终止条件
    1 + 1 +  6                                # 归来
    8
"""


def Fibonacci(n):
    if n > 1:  # 步1
        return Fibonacci(n-1) + Fibonacci(n-2)  # 步2 步3
    return 1


if __name__ == '__main__':
    print(Fibonacci(5))
