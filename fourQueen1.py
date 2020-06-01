def is_rule(queen_tup, new_queen):
    """判断棋子是否符合规则"""
    for index, queen in enumerate(queen_tup):
        if abs(new_queen - queen) in (len(queen_tup) - index, 0):  # 判断表达式
            return False
    return True


def arrange_queen(num, queen_tup=list()):
    """
    :param num:棋盘的的行数，当然数值也等于棋盘的列数
    :param queen_tup: 设置一个空队列，用于保存符合规则的棋子的信息
    """

    for new_queen in range(num):  # 遍历一行棋子的每一列

        if is_rule(queen_tup, new_queen):  # 判断是否冲突

            if len(queen_tup) == num - 1:  # 判断是否是最后一行
                yield [new_queen]  # yield关键字
            else:
                # 若果不是最后一行，递归函数接着放置棋子
                for result in arrange_queen(num, queen_tup + [new_queen]):
                    yield [new_queen] + result


if __name__ == '__main__':
    for i in arrange_queen(8):
        print(i)