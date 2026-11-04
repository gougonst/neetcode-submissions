class Node:
    def __init__(self, val: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = Node(-1)

    def addNode(self, val: int) -> None:
        cur = self.root
        while cur.next is not None:
            if cur.next.val == val:
                return
            cur = cur.next
        cur.next = Node(val)

    def removeNode(self, val: int) -> None:
        prev, cur = self.root, self.root.next
        while cur and cur.val != val:
            prev = cur
            cur = cur.next

        if cur is None:
            return
        next = cur.next
        prev.next = next

    def get(self, val: int) -> bool:
        cur = self.root.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False


class MyHashSet:

    HASH_SIZE = 100

    def __init__(self):
        self.hashset = [LinkedList() for _ in range(self.HASH_SIZE)]

    def _hash(self, key: int) -> int:
        return key % self.HASH_SIZE

    def add(self, key: int) -> None:
        self.hashset[self._hash(key)].addNode(key)

    def remove(self, key: int) -> None:
        self.hashset[self._hash(key)].removeNode(key)

    def contains(self, key: int) -> bool:
        return self.hashset[self._hash(key)].get(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)