# coding=utf-8
# @Time    : 2019-03-29 17:24
# @Author  : 张嘉麒
# @File    : calculating_pi.py


"""
求PI的值
Leibniz formula效率更高
"""
def calculating_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)

        denominator += 2.0
        operation *= -1.0

    return pi

if __name__ == "__main__":
    print(calculating_pi(100000000))