# input_init.py
# 输入与初始化

import os


def input_init():
    # 清除终端的屏幕
    os.system("cls" if os.name == "nt" else "clear")

    # 输入棋盘大小
    n = int(input("board size:"))

    # 输入每行的棋子排布规则
    global row_rules  # 声明全局变量
    row_rules = []  # 先清空列表
    for i in range(n):
        print(f"row {i + 1}:", end=" ")  # 打印行号提示，并且换行符使用空格
        row_rules.append(list(map(int, input().split())))
    print()  # 打印一个空行分割

    # 输入每列的棋子排布规则
    global col_rules  # 声明全局变量
    col_rules = []  # 先清空列表
    for i in range(n):
        print(f"col {i + 1}:", end=" ")  # 打印列号提示，并且换行符使用空格
        col_rules.append(list(map(int, input().split())))
    print()  # 打印一个空行分割

    # 检查输入是否正确
    ok = True
    sum_row = sum(sum(row) for row in row_rules)
    sum_col = sum(sum(col) for col in col_rules)
    if sum_row != sum_col:
        ok = False

    # 返回棋盘的大小，规则
    return n, row_rules, col_rules, ok
