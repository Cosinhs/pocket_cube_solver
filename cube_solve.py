#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二阶魔方 (2x2x2) BFS 最优解还原程序
状态表示：长度为24的字符串，每4个字符代表一个面。
顺序：U(白) F(绿) R(红) B(蓝) L(橙) D(黄)
"""

from collections import deque

# 目标状态（已还原的魔方）
GOAL = "WWWWGGGGRRRRBBBBOOOOYYYY"

# ---------- 旋转函数（每个函数接收字符串，返回新字符串，不修改原状态） ----------

def move_U(state):
    a = list(state)
    # U 面顺时针
    a[0], a[1], a[2], a[3] = a[2], a[0], a[3], a[1]
    # 相邻四个面的顶层
    a[4], a[5], a[8], a[9], a[12], a[13], a[16], a[17] = \
        a[16], a[17], a[4], a[5], a[8], a[9], a[12], a[13]
    return ''.join(a)

def move_U_prime(state):
    a = list(state)
    a[0], a[1], a[2], a[3] = a[1], a[3], a[0], a[2]
    a[4], a[5], a[8], a[9], a[12], a[13], a[16], a[17] = \
        a[8], a[9], a[12], a[13], a[16], a[17], a[4], a[5]
    return ''.join(a)

def move_R(state):
    a = list(state)
    # R 面顺时针
    a[8], a[9], a[10], a[11] = a[10], a[8], a[11], a[9]
    # 相邻面
    a[1], a[3], a[5], a[7], a[21], a[23], a[13], a[15] = \
        a[5], a[7], a[21], a[23], a[13], a[15], a[1], a[3]
    return ''.join(a)

def move_R_prime(state):
    a = list(state)
    a[8], a[9], a[10], a[11] = a[9], a[11], a[8], a[10]
    a[1], a[3], a[5], a[7], a[21], a[23], a[13], a[15] = \
        a[13], a[15], a[1], a[3], a[5], a[7], a[21], a[23]
    return ''.join(a)

def move_F(state):
    a = list(state)
    # F 面顺时针
    a[4], a[5], a[6], a[7] = a[6], a[4], a[7], a[5]
    # 相邻面
    a[2], a[3], a[8], a[10], a[20], a[21], a[17], a[19] = \
        a[17], a[19], a[2], a[3], a[8], a[10], a[20], a[21]
    return ''.join(a)

def move_F_prime(state):
    a = list(state)
    a[4], a[5], a[6], a[7] = a[5], a[7], a[4], a[6]
    a[2], a[3], a[8], a[10], a[20], a[21], a[17], a[19] = \
        a[8], a[10], a[20], a[21], a[17], a[19], a[2], a[3]
    return ''.join(a)


# ---------- BFS 搜索最优解 ----------

def bfs_solve(start_state):
    """
    使用 BFS 从 start_state 找到还原步骤（字符数组）。
    返回步骤列表，例如 ['U', "R'", 'F']，无解则返回 None。
    """
    if start_state == GOAL:
        return []

    queue = deque()
    queue.append((start_state, []))  # (当前状态, 步骤字符数组)
    visited = {start_state}

    # 定义可用的转动操作
    moves = [
        ('U', move_U), ("U'", move_U_prime),
        ('R', move_R), ("R'", move_R_prime),
        ('F', move_F), ("F'", move_F_prime),
    ]

    while queue:
        state, path = queue.popleft()
        for move_name, move_func in moves:
            new_state = move_func(state)
            if new_state == GOAL:
                return path + [move_name]  # 找到最优解
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move_name]))

    return None


# ---------- 测试 ----------

if __name__ == "__main__":
    print("目标状态:", GOAL)

    # 制造一个打乱：先转 U，再转 R
    scrambled = move_U_prime(move_F(move_R(move_R(move_U(GOAL)))))
    print("打乱状态:", scrambled)

    print("\n正在用 BFS 搜索最优解，请稍候...")
    solution = bfs_solve(scrambled)

    if solution is not None:
        print("✅ 找到最优解！步数:", len(solution))
        print("📋 步骤（字符数组）:", solution)
        # 验证：按步骤执行，看是否回到目标
        current = scrambled
        for step in solution:
            if step == 'U': current = move_U(current)
            elif step == "U'": current = move_U_prime(current)
            elif step == 'R': current = move_R(current)
            elif step == "R'": current = move_R_prime(current)
            elif step == 'F': current = move_F(current)
            elif step == "F'": current = move_F_prime(current)
        print("🔍 验证还原结果:", "成功 ✅" if current == GOAL else "失败 ❌")
    else:
        print("❌ 未找到解法")