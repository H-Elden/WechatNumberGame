# progressbar.py
# 显示进度条

import sys


def print_bar(board_list):
    """
    计算进度百分比，并打印进度条。
    @参数:
        board_list - 棋盘
    """
    # 初始化一个空字符串，用于存储二进制位
    binary_string = ""

    # 计数器，用于跟踪已处理的数字数量
    count = 0

    # 遍历二维列表
    for row in board_list:
        for num in row:
            # 当处理的数字少于14个时，继续添加二进制位
            if count < 14:
                binary_string += str(num)
                count += 1
            else:
                # 如果已经处理了14个数字，则停止循环
                break
    # 将二进制字符串转换为整数
    binary_integer = int(binary_string, 2)

    percentage = binary_integer / ((1 << 14) - 1)
    # 由于只取了高14二进制位，所以percentage == 1.0时不一定进度100%
    if percentage == 1.0:
        percentage = 0.9999
    print_progress_bar(percentage)


def print_progress_bar(progress):
    """
    Call in a loop to create terminal progress bar with color.
    @param:
        progress - Required : the progress as a fraction between 0 and 1 (Float)
    """
    # Set the length of the progress bar
    length = 50
    # Convert progress to percentage and then to an integer for the bar length
    percentage_int = int(progress * length)
    # Create the progress bar string
    green_bar = "\033[92m" + "-" * percentage_int + "\033[0m"
    red_bar = "\033[91m" + "-" * (length - percentage_int) + "\033[0m"
    # Create the full progress bar with start and end symbols
    if progress == 1.0:
        bar = "\033[92m|" + green_bar + "\033[92m|"  # Both ends green for 100%
    else:
        bar = "\033[92m|" + green_bar + red_bar + "\033[91m|"
    # Create the percentage string
    percent = f"{progress:.2%}"
    # Write the progress bar to stdout with light blue color for percentage
    sys.stdout.write(f"\r{bar} \033[94m{percent}\033[0m")
    # Flush stdout to ensure the output is printed immediately
    sys.stdout.flush()
    # If progress is 100%, print "Complete!" and a newline
    if progress == 1.0:
        print(f"\r{bar} \033[92m{percent}\033[0m")
        print("Complete!")
