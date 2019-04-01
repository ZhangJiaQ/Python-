# coding=utf-8
# @Time    : 2019-03-29 17:34
# @Author  : 张嘉麒
# @File    : towers_of_hanoi.py
from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):

    """
    实现一个先入后出的栈结构
    """

    def __init__(self):
        self._container: List[T] = []

    def push(self, item: T):
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        # 首先我们需要将第1个到n-1个的环从begin柱移动到temp柱上
        hanoi(begin, temp, end, n - 1)
        # 接下来我们需要将第N个环从begin柱移动到end柱上
        hanoi(begin, end, temp, 1)
        # 最后吧第一个到n-1个环从temp柱上移动到end柱上
        hanoi(temp, end, begin, n - 1)

if __name__ == "__main__":
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a, tower_b, tower_c)