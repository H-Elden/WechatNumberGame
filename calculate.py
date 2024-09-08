# calculate.py
# 计算答案的函数

import time


from progressbar import print_progress_bar
from progressbar import print_bar


def cal(board_size, row_rules, col_rules):
    print("Calculating...")
    print_progress_bar(0)
    # 记录开始计算时的时间
    start_time = time.time()
    # 解决棋盘问题
    solution = solve_chessboard(board_size, row_rules, col_rules)
    # 记录结束计算时的时间
    end_time = time.time()
    calculation_time = end_time - start_time
    print_progress_bar(1)
    print(f"Calculation time: {calculation_time:.6f} s")
    return solution


def solve_chessboard(n, row_rules, col_rules):
    # 初始化棋盘
    board = [[0] * n for _ in range(n)]

    # 检查放置是否满足行列规则
    def is_valid(board_row, row_rule, col):
        # 处理规则为0的情况
        if row_rule == [0]:
            if sum(board_row) == 0:
                return True
            else:
                return False

        remain_cell = n - (col + 1)  # 剩余格子数
        remain_piece = sum(row_rule) - sum(board_row)  # 剩余棋子数
        space = len(row_rule) - 1  # 至少空格数

        # 特殊处理全为0的情况
        if sum(board_row) == 0:
            # 剩余格子数 < 棋子数 + 至少空格数
            if remain_cell < remain_piece + space:
                return False
            else:
                return True

        i = 0
        index = 0  # 棋子组编号
        while i <= col:
            if board_row[i] == 1:
                index += 1
                count = 0  # 棋子组的棋子数
                while i <= col and board_row[i] == 1:
                    count += 1
                    i += 1

                # 检查是否合法
                if index > len(row_rule):  # 棋子组数超过规则
                    return False
                if i == col + 1:  # 最后一个组
                    # 棋子数不超过即可
                    if count > row_rule[index - 1]:
                        return False
                else:
                    # 严格相等
                    if count != row_rule[index - 1]:
                        return False
            else:
                i += 1

        # 剩余的格子不够用：剩余格子数 < 剩余棋子数 + 至少的空格数
        space -= index
        if board_row[col] == 1:
            space += 1
        if remain_cell < remain_piece + space:
            return False

        # 如果所有比较都通过，则返回True
        return True

    # 深度优先搜索
    def dfs(row=0, col=0):
        if row == n:
            return True  # 找到一个解

        for i in range(2):
            board[row][col] = i
            # 判断行列是否均符合规则
            if is_valid(board[row], row_rules[row], col) and is_valid(
                [row[col] for row in board], col_rules[col], row
            ):
                if dfs(row + (col + 1) // n, (col + 1) % n):
                    return True

        # 打印进度条
        if row * n + col < 14:
            print_bar(board)
        return False

    if dfs():
        return board
    else:
        return None
