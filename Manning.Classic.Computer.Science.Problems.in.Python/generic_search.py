# coding=utf-8
# @Time    : 2019-04-02 21:58
# @Author  : 张嘉麒
# @File    : generic_search.py
from collections import deque
from heapq import heappush, heappop
from typing import Generic, List, TypeVar, Optional, Callable, Set, Deque, Dict

from maze_solving import Maze, MazeLocation, manhattan_distance

T = TypeVar('T')


class Stack(Generic[T]):
    # 栈

    def __init__(self) -> None:
        self._container: List[T] = []

    def pop(self) -> T:
        return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

    def __repr__(self) -> str:
        return repr(self._container)

    @property
    def empty(self) -> bool:
        return not self._container


class Queue(Generic[T]):
    # 队列
    def __init__(self) -> None:
        self._container: Deque[T] = deque()

    @property
    def empty(self) -> bool:
        # 一个方法变成属性调用的
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)


class PriorityQueue(Generic[T]):

    def __init__(self) -> None:
        self._container: List = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):

    def __init__(self, state: T, parent: T, cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: T):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:

    # 初始化栈
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))

    # 初始化集合
    explored: Set[T] = {initial}

    # 不停循环，直到所有的能够走动的点被遍历
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # 找到终点，返回
        if goal_test(current_state):
            return current_node

        # 检查下一个目的地是否没有被探索过,没有则加入进行探索
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # 初始化栈
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))

    # 初始化集合
    explored: Set[T] = {initial}

    # 不停循环，直到所有的能够走动的点被遍历
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # 找到终点，返回
        if goal_test(current_state):
            return current_node

        # 检查下一个目的地是否没有被探索过,没有则加入进行探索
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]],
          heuristic:Callable[[T], float]) -> Optional[Node[T]]:

    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


def node_to_path(node: Node[T]) -> List[T]:
    # 将路径汇总返回
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


if __name__ == "__main__":
    # 测试深度优先遍历  栈辅助
    m: Maze = Maze()
    print(m)
    solution1: Optional[Node[MazeLocation]] =  dfs(m.start, m.goal_test, m.successors)

    if solution1 is None:
        print("No path")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)

    # 测试广度优先遍历  队列辅助
    solution2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)

    if solution2 is None:
        print("No path")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)

    # 测试A*算法  优先级队列辅助
    distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test,m.successors, distance)
    if solution3 is None:
        print("No solution found using A*!")
    else:
        path3: List[MazeLocation] = node_to_path(solution3)
        m.mark(path3)
        print(m)