# result.py
# 计算结果的输出

import matplotlib.pyplot as plt
import numpy as np


def plot_chessboard(s, figsize=(8, 8)):
    n = len(s[0])

    # 创建一个新的图像
    fig, ax = plt.subplots(figsize=figsize)

    # 创建一个n*n的网格
    for i in range(n):
        for j in range(n):
            # 定义颜色
            color = "palegoldenrod" if s[i][j] == 0 else "green"

            # 绘制矩形
            rect = plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor="white")
            ax.add_patch(rect)

    # 设置xy轴主要刻度线的位置
    ax.set_xticks(np.arange(0.5, n + 1, 1))
    ax.set_yticks(np.arange(0.5, n + 1, 1))
    # 设置xy轴次要刻度线的位置
    step = 1
    if n >= 8:
        if n % 4 == 0:
            step = 4
        elif n % 5 == 0:
            step = 5
    ax.set_xticks(np.arange(0, n + 1, step), minor=True)
    ax.set_yticks(np.arange(0, n + 1, step), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=2)

    # 设置坐标轴不可见
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # 调整图像的范围和移除刻度标签
    ax.set_xlim([0, n])
    ax.set_ylim([n, 0])
    ax.tick_params(axis="both", which="both", length=0)

    plt.show()


def result_show(solution):
    # 打印解决方案
    if solution:
        print("solution:")  # 打印编号
        for row in solution:
            print(" ".join(str(cell) for cell in row))
        plot_chessboard(solution, figsize=(6, 6))
    else:
        print("\033[91m" + "No solution found." + "\033[0m")
        input("press Enter to continue...")
