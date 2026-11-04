class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        self._start = Node(0, 0)
        self._end = Node(0, 0)
        self._start.next = self._end
        self._end.prev = self._start

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        prev = self._end.prev
        prev.next = node
        node.prev = prev
        node.next = self._end
        self._end.prev = node

    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self.remove(self._cache[key])
        self._cache[key] = Node(key, value)
        self.insert(self._cache[key])

        if len(self._cache) > self._capacity:
            lru = self._start.next
            self.remove(lru)
            del self._cache[lru.key]

