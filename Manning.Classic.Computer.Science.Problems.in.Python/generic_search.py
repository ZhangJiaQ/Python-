# coding=utf-8
# @Time    : 2019-04-02 21:58
# @Author  : 张嘉麒
# @File    : generic_search.py
from typing import Generic, List, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def pop(self) -> T:
        return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

    def __repr__(self) -> str:
        return repr(self._container)

    def empty(self) -> bool:
        return not self._container

class Node(Generic[T]):
    def __init__(self):
        pass


def dfs():
    return None

def bfs():
    return None

def node_to_path():
    return None

def astar():
    return None