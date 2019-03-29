# coding=utf-8
# @Time    : 2019-03-29 10:39
# @Author  : 张嘉麒
# @File    : fibonacci.py
import time
from typing import Dict
from functools import lru_cache
memo: Dict[int, int] = {0: 0, 1: 1}

def timeit(func):
    def _func(*args):
        startTime = time.time()
        func(*args)
        endTime = time.time()
        print(endTime - startTime)
    return _func

def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)

def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    """
    在functools这个模块中，有lru_cache这个一个神奇的装饰器存在。
    functools.lru_cache的作用主要是用来做缓存，他能把相对耗时的函数结果进行保存，避免传入相同的参数重复计算。
    同时，缓存并不会无限增长，不用的缓存会被释放。
    """
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)

def fib4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib5(n: int) -> int:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next



if __name__ == "__main__":
    startTime = time.time()
    # fib1(30)  # 计算斐波那契数列40耗时40s  调用栈深度不能超过1000
    # fib2(800)   # 计算斐波那契数列800耗时0.0009s  需要维护一个长度为800的字典
    # fib3(30)     # lru_cache的作用主要是用来做缓存，他能把相对耗时的函数结果进行保存，避免传入相同的参数重复计算。
    # fib4(8000)   # 计算斐波那契数列8000耗时0.0009s  需要维护一个长度为800的字典
    # for i in fib5(8000):  # 生成器
    #     pass
    endTime = time.time()
    print(endTime - startTime)
