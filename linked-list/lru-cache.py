from typing import Optional, Self


class Node:
    key: int
    val: int
    prev: Optional[Self]
    next: Optional[Self]

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    cache: dict[int, Node]
    capacity: int
    left: Node
    right: Node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next

        if next:
            next.prev = prev

    def insert(self, node: Node):
        prev = self.right.prev
        next = self.right

        next.prev = node

        if prev:
            prev.next = node

        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            if lru:
                self.remove(lru)
                del self.cache[lru.key]
