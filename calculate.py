# calculate.py
# 计算答案的函数

import time
import copy


from progressbar import print_progress_bar


def cal(board_size, row_rules, col_rules):
    print("Calculating...")
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
    board_row_dict = {}  # 创建字典实现记忆化搜索
    solution = []

    # 初始化某行
    def init_board_row(total_ones):
        if total_ones in board_row_dict:
            return board_row_dict[total_ones]
        elif total_ones == 0:
            # 只有1种情况，全为0
            board_row_dict[0] = [[0] * n]
            return board_row_dict[0]
        else:

            def dfs(col, remaining_ones, current_row):
                if col == n:
                    if remaining_ones == 0:
                        yield current_row.copy()
                    return
                if remaining_ones > 0:
                    # 在当前列放1
                    current_row[col] = 1
                    yield from dfs(col + 1, remaining_ones - 1, current_row)
                    # 回溯，置零
                    current_row[col] = 0
                # 在当前列放0
                yield from dfs(col + 1, remaining_ones, current_row)

            # 初始化
            board_row = [0] * n
            # 使用dfs搜索，并记忆
            board_row_dict[total_ones] = list(dfs(0, total_ones, board_row))
            return board_row_dict[total_ones]

    # 检查放置是否满足行规则
    def is_valid_row_pattern(board_row, pattern):
        groups = []
        i = 0
        while i < len(board_row):
            if board_row[i] == 1:
                count = 0
                while i < len(board_row) and board_row[i] == 1:
                    count += 1
                    i += 1
                groups.append(count)
            else:
                i += 1
        # 如果列表为空
        if not groups:
            groups = [0]
        # 首先比较两个列表的长度是否相等
        if len(groups) != len(pattern):
            return False

        # 然后逐个比较列表中的数字
        for group_size, pattern_size in zip(groups, pattern):
            if group_size != pattern_size:
                return False

        # 如果所有比较都通过，则返回True
        return True

    # 检查放置是否满足列规则
    def is_valid_col(current_row):
        for col in range(n):
            groups = []
            row = 0
            while row <= current_row:
                if board[row][col] == 1:
                    count = 0
                    while row <= current_row and board[row][col] == 1:
                        count += 1
                        row += 1
                    groups.append(count)
                else:
                    row += 1

            # 保证剩下的行数够放棋子
            if n - (current_row + 1) < sum(col_rules[col]) - sum(groups):
                return False

            # 处理groups长度为0的特殊情况
            if len(groups) == 0:
                continue

            # 处理最后一行
            if current_row == n - 1:
                # 首先比较两个列表的长度
                if len(groups) != len(col_rules[col]):
                    return False
                # 然后逐个比较
                for i in range(len(groups)):
                    if groups[i] != col_rules[col][i]:
                        return False

            # 不是最后一行
            else:
                # 首先比较两个列表的长度
                if len(groups) > len(col_rules[col]):
                    return False
                # 逐个比较，最后一个数字除外
                for i in range(len(groups) - 1):
                    if groups[i] != col_rules[col][i]:
                        return False
                # 最后一个数字
                last_index = len(groups) - 1
                # 如果当前行棋子刚刚放，最后一个棋子组应小于等于rules
                if board[current_row][col] == 1:
                    if groups[last_index] > col_rules[col][last_index]:
                        return False
                # 否则，应当严格等于
                else:
                    if groups[last_index] != col_rules[col][last_index]:
                        return False
        # 如果所有比较都通过，则返回True
        return True

    # 深度优先搜索
    def dfs(row=0):
        if row == n:
            solution.append(copy.deepcopy(board))
            return  # 找到一个解
        board_row = init_board_row(sum(row_rules[row]))
        for index, situation in enumerate(board_row):
            if row == 0:
                print_progress_bar(index / len(board_row))
            if is_valid_row_pattern(situation, row_rules[row]):
                # 尝试放置棋子
                board[row] = situation
                # 如果当前行满足列要求
                if is_valid_col(row):
                    # 递归到下一行
                    dfs(row + 1)
                    # 回溯，也可以不清零
                    board[row] = [0] * n

    dfs()
    return solution
