# coding=utf-8
# @Time    : 2019-05-06 17:00
# @Author  : 张嘉麒
# @File    : array_and_linked_structures.py
from typing import TypeVar

T = TypeVar('T', int, str)

class Array():

    def __init__(self, capacity, fill_value=None):
        self.item = list()
        for d in range(capacity):
            self.item.append(fill_value)

    def len(self):
        return len(self.item)

    def str(self):
        return str(self.item)

    def iter(self):
        return iter(self.item)

    def getitem(self, index):
        return self.item[index]

    def setitem(self, index, new_item):
        self.item[index] = new_item


class Node():

    def __init__(self, data, next=None):

        self.data = data
        self.next = next



def search_node(head: Node, key: T) -> int:
    # 查询key是否存在与链表中
    probe: Node = head
    while probe.next != None and probe.data != key:
        probe = probe.next
    if probe.data == key:
        return 1
    else:
        return 0

def insert_to_beginning(head: Node, key: T) -> None:
    # 链表插入至首部
    new_node = Node(key)
    if head.next == None:
        head.next = new_node
    else:
        new_node.next = head.next
        head.next = new_node

def insert_to_end(head: Node, key: T) -> None:
    # 链表插入至首部
    new_node = Node(key)
    if head.next == None:
        head.next = new_node
    else:
        while head.next != None:
            head = head.next
        head.next = new_node

def remove_at_end(head: Node) -> None:
    # 移除表尾元素
    if head.next is None:
        head = None
    else:
        while head.next.next != None:
            head = head.next
        head.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head
        slow = head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)
    head = node5
    insert_to_end(head, 6)