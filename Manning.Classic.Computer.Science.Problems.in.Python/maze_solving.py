# coding=utf-8
# @Time    : 2019-04-02 21:52
# @Author  : 张嘉麒
# @File    : maze_solving.py

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt


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

    def mark(self, path: List[MazeLocation]):
        # 标记走过的路程
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        # 清除标记
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        # 求出可走路径
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 > 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 > 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))

        return locations

    def __str__(self):
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output


def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    # 直线距离
    def distance(ml: MazeLocation):
        xdist: int = ml.column - goal.column
        ydist: int = ml.row - goal.row
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance


def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    # 最近距离
    def distance(ml: MazeLocation):
        xdist: int = abs(ml.column - goal.column)
        ydist: int = abs(ml.row - goal.row)
        return (xdist + ydist)
    return distance