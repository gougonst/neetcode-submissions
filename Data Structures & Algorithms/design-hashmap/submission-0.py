class Node:
    def __init__(self, key: int, val: int):
        self.key: int = key
        self.val: int = val
        self.next: Node = None


class MyHashMap:

    MAP_LEN = 1000

    def __init__(self):
        self._hashMap: List[Optional[Node]] = [None] * self.MAP_LEN

    def put(self, key: int, value: int) -> None:
        hashValue = self._calcHashValue(key)
        root = self._hashMap[hashValue]
        if not root:
            self._hashMap[hashValue] = Node(key, value)
        else:
            node = root
            while node.next and node.key != key:
                node = node.next
            if node.key == key:
                node.val = value
            else:
                node.next = Node(key, value)

    def get(self, key: int) -> int:
        hashValue = self._calcHashValue(key)
        root = self._hashMap[hashValue]
        if not root:
            return -1
        
        node = root
        while node.next and node.key != key:
            node = node.next
        if node.key == key:
            return node.val
        else:
            return -1

    def remove(self, key: int) -> None:
        hashValue = self._calcHashValue(key)
        root = self._hashMap[hashValue]
        if not root:
            return

        if root.key == key:
            self._hashMap[hashValue] = root.next
        else:
            prev, cur = root, root.next
            while cur and cur.key != key:
                cur = cur.next
            if cur:
                prev.next = cur.next

    def _calcHashValue(self, val: int) -> int:
        return val % self.MAP_LEN
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)