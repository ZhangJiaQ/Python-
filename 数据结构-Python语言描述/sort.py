# coding=utf-8
# @Time    : 2019-04-15 16:02
# @Author  : 张嘉麒
# @File    : 1test.py
from typing import List

def minimum_swaps(arr):
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


def find_min(target_list: List):
    # 查询数组中最小值
    targetLen: int = len(target_list)
    if targetLen == 0:
        raise ValueError("传入数组长度不能为0")
    minIndex: int = 0
    currentIndex: int = 0
    while currentIndex < targetLen:
        if target_list[currentIndex] < target_list[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return target_list[minIndex]


def find_target(target:int, target_list: List):
    # 查询目标元素是否存在于数组中
    position: int = 0
    for index, data in enumerate(target_list):
        if data == target:
            return index
    return -1


def binary_search(target: int, sorted_list: List):
    # 二分搜索
    left: int = 0
    right: int = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[right] == target:
            return 1
        elif sorted_list[right] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def selection_sort(unsorted_list: List):
    # 选择排序  两次循环  O(n^2)  与接下来所有的元素比较，如果将元素比后面元素大向后移动
    firstIndex: int = 0
    while firstIndex < len(unsorted_list) - 1:
        secondIndex: int = firstIndex + 1
        while secondIndex < len(unsorted_list):
            if unsorted_list[firstIndex] > unsorted_list[secondIndex]:
                unsorted_list[firstIndex], unsorted_list[secondIndex] = unsorted_list[secondIndex], unsorted_list[firstIndex]
            secondIndex += 1
        firstIndex += 1
    return unsorted_list


def bubble_sort(unsorted_list: List):
    # 冒泡排序  只与当前元素的下一个元素作比较，如果比下一个元素大则向前移动一位 在部分元素有规律的情况下有优势
    for index in range(len(unsorted_list)):
        for index2 in range(len(unsorted_list) - index - 1):
            if unsorted_list[index2 + 1] < unsorted_list[index2]:
                unsorted_list[index2 + 1], unsorted_list[index2] = unsorted_list[index2], unsorted_list[index2 + 1]
    return unsorted_list


def insertion_sort(unsorted_list: List):
    # 插入排序  从第二个元素（下标为1）开始，找到比他小的元素调换位置
    i = 1
    while i < len(unsorted_list):
        # 设置监视哨
        item = unsorted_list[i]
        need_left = i - 1
        while need_left >= 0:
            if item < unsorted_list[need_left]:
                unsorted_list[need_left + 1] =  unsorted_list[need_left]
                need_left -= 1
            else:
                break
        unsorted_list[need_left + 1] = item
        i += 1
    return unsorted_list


def quick_sort(unsorted_list: List, left: int, right: int):
    # 快速排序
    if left < right:
        pivotLocation = partition(unsortList, left, right)
        quick_sort(unsortList, left, pivotLocation - 1)
        quick_sort(unsortList, pivotLocation + 1, right)

def partition(unsorted_list: List, left: int, right: int):
    # 快速排序的分割
    # 找到监视哨，将大于监视哨的值放置于监视哨右边，小于监视哨的值放置于监视哨左边
    middle: int = (left + right) // 2
    pivot: int = unsorted_list[middle]
    # 将监视哨放置在尾部节点
    unsorted_list[middle], unsorted_list[right] = unsorted_list[right], unsorted_list[middle]

    # 执行偏移量
    boundary: int = left
    for index in range(left, right):
        if unsorted_list[index] < pivot:
            unsorted_list[index], unsorted_list[boundary] = unsorted_list[boundary], unsorted_list[index]
            boundary += 1

    unsorted_list[right], unsorted_list[boundary] = unsorted_list[boundary], unsorted_list[right]
    return boundary


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    unsortList = [2, 3, 1, 5, 4]
    # print(findMin(arr))
    # print(findTarget(1, arr))
    # print(binarySearch(2, arr))
    # print(selectionSort(unsortList))
    # print(bubble_sort(unsortList))
    # print(insertion_sort(unsortList))
    quick_sort(unsortList, 0, len(unsortList) - 1)
    print(unsortList)