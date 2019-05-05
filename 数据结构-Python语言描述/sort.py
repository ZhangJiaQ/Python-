# coding=utf-8
# @Time    : 2019-04-15 16:02
# @Author  : 张嘉麒
# @File    : 1test.py
from typing import List


def minimumSwaps(arr):
    swap = 0
    # 设定data -> index的dict
    swap_map = {data: index for index, data in enumerate(arr)}


    for index, data in enumerate(arr):
        print(data, "data")

        if index + 1 != data:
            # 找到需要替换的索引
            replace_index = swap_map[index+1]
            arr[replace_index], arr[index] = arr[index], arr[replace_index]

            # 更改data -> replace dict
            swap_map[data] = replace_index
            swap_map[arr[index]] = index + 1
            swap += 1
    return swap


def findMin(targetList: List):
    # 查询数组中最小值
    targetLen: int = len(targetList)
    if targetLen == 0:
        raise ValueError("传入数组长度不能为0")
    minIndex: int = 0
    currentIndex: int = 0
    while currentIndex < targetLen:
        if targetList[currentIndex] < targetList[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return targetList[minIndex]


def findTarget(target:int, targetList: List):
    # 查询目标元素是否存在于数组中
    position: int = 0
    for index, data in enumerate(targetList):
        if data == target:
            return index
    return -1


def binartSearch(target: int, sortedList: List):
    # 二分搜索
    left: int = 0
    right: int = len(sortedList) - 1
    while left <= right:
        mid = (left + right) // 2
        if sortedList[right] == target:
            return 1
        elif sortedList[right] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def selectionSort(unSortedList: List):
    # 选择排序  两次循环  O(n^2)  与接下来所有的元素比较，如果将元素比后面元素大向后移动
    firstIndex: int = 0
    while firstIndex < len(unSortedList) - 1:
        secondIndex: int = firstIndex + 1
        while secondIndex < len(unSortedList):
            if unSortedList[firstIndex] > unSortedList[secondIndex]:
                unSortedList[firstIndex], unSortedList[secondIndex] = unSortedList[secondIndex], unSortedList[firstIndex]
            secondIndex += 1
        firstIndex += 1
    return unSortedList


def bubbleSort(unSortedList: List):
    # 冒泡排序  只与当前元素的下一个元素作比较，如果比下一个元素大则向前移动一位
    for index in range(len(unSortedList)):
        for index2 in range(len(unSortedList) - index - 1):
            if unSortedList[index2 + 1] < unSortedList[index2]:
                unSortedList[index2 + 1], unSortedList[index2] = unSortedList[index2], unSortedList[index2 + 1]
    return unSortedList


def insertionSort(unSortedList: List[int]):
    # 插入排序
    pass


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    unsortList = [2, 1, 3, 5, 4]
    # print(findMin(arr))
    # print(findTarget(1, arr))
    # print(binartSearch(2, arr))
    # print(selectionSort(unsortList))
    print(bubbleSort(unsortList))