# main.py

# 多文件管理，导入其他模块的函数、全局变量
from input_init import input_init
from calculate import cal
from result import result_show


def main():
    while True:
        # 输入和初始化
        board_size, row_rules, col_rules = input_init()
        # 计算
        solution = cal(board_size, row_rules, col_rules)
        # 显示答案
        result_show(solution)


if __name__ == "__main__":
    main()
