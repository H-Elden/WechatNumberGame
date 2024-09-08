# main.py

# 多文件管理，导入其他模块的函数、全局变量
from input_init import input_init
from calculate import cal
from result import result_show


def main():
    while True:
        # 输入和初始化
        board_size, row_rules, col_rules, input_ok = input_init()

        if input_ok == 1:
            # 计算
            solution = cal(board_size, row_rules, col_rules)
            # 显示答案
            result_show(solution)
        elif input_ok == 2:
            # 触发reset
            continue
        else:
            print("\033[91m" + "INPUT ERROR!" + "\033[0m")
            input("press Enter to continue...")


if __name__ == "__main__":
    main()
