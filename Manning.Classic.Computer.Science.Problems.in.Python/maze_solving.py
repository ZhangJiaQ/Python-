# coding=utf-8
# @Time    : 2019-04-02 21:52
# @Author  : 张嘉麒
# @File    : maze_solving.py

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, bfs, node_to_path, astar, Node


"""
通过迷宫来讲述
深度优先搜索
广度优先搜索
A*算法
"""

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns:int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)]for r in range(rows)]
        # 初始化迷宫
        self._randomly_fill(rows, columns, sparseness)

        # 初始化起点和终点
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    # 初始化无法行走的路
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output