# input_init.py
# 输入与初始化

import os
import sys


def input_init():
    # 清除终端的屏幕
    os.system("cls" if os.name == "nt" else "clear")

    # 输入棋盘大小
    while True:
        try:
            n_str = input("board size:")
            if n_str == "exit":
                sys.exit(0)
            n = int(n_str)
            if n <= 0:
                raise ValueError("Board size must be a positive integer.")
            break
        except ValueError as e:
            print(
                f"\033[91mInvalid input: {e}. Please enter a positive integer.\033[0m"
            )

    # 输入每行的棋子排布规则
    row_rules = []  # 先清空列表
    i = 0
    while i < n:
        while True:
            try:
                print(f"row {i + 1}:", end=" ")  # 打印行号提示，并且换行符使用空格
                str_input = input()
                if str_input == "undo":
                    if i > 0:
                        i -= 2
                        row_rules.pop()
                        break
                    else:
                        raise ValueError("You cannot use this command here.")
                if str_input == "reset":
                    return n, None, None, 2
                if str_input == "exit":
                    sys.exit(0)
                row_input = list(map(int, str_input.split()))
                if not all(x >= 0 and x <= n for x in row_input):
                    raise ValueError(
                        f"All numbers must be within the range of [0,{n}]."
                    )
                if sum(row_input) > n:
                    raise ValueError(
                        f"The sum of all numbers must be within the range of [0,{n}]."
                    )
                if 0 in row_input and len(row_input) > 1:
                    raise ValueError("You can only enter one zero.")
                row_rules.append(row_input)
                break
            except ValueError as e:
                print(
                    f"\033[91mInvalid input: {e}. Please enter nonnegative integers separated by spaces.\033[0m"
                )
        i += 1
    print()  # 打印一个空行分割

    # 输入每列的棋子排布规则
    col_rules = []  # 先清空列表
    i = 0
    while i < n:
        while True:
            try:
                print(f"col {i + 1}:", end=" ")  # 打印行号提示，并且换行符使用空格
                str_input = input()
                if str_input == "undo":
                    if i > 0:
                        i -= 2
                        col_rules.pop()
                        break
                    else:
                        raise ValueError("You cannot use this command here.")
                if str_input == "reset":
                    return n, None, None, 2
                if str_input == "exit":
                    sys.exit(0)
                col_input = list(map(int, str_input.split()))
                if not all(x >= 0 and x <= n for x in col_input):
                    raise ValueError(
                        f"All numbers must be within the range of [0,{n}]."
                    )
                if sum(col_input) > n:
                    raise ValueError(
                        f"The sum of all numbers must be within the range of [0,{n}]."
                    )
                if 0 in row_input and len(col_input) > 1:
                    raise ValueError("You can only enter one zero.")
                col_rules.append(col_input)
                break
            except ValueError as e:
                print(
                    f"\033[91mInvalid input: {e}. Please enter nonnegative integers separated by spaces.\033[0m"
                )
        i += 1
    print()  # 打印一个空行分割

    # 检查输入是否正确
    ok = 1
    sum_row = sum(sum(row) for row in row_rules)
    sum_col = sum(sum(col) for col in col_rules)
    if sum_row != sum_col:
        ok = 0

    # 返回棋盘的大小，规则
    return n, row_rules, col_rules, ok
