class Node:
    def __init__(self, key: int = -1, val: int = -1, next = None):
        self.key: int = key
        self.val: int = val
        self.next: Node = next


class MyHashMap:

    MAP_LEN = 1000

    def __init__(self):
        self._hashMap: List[Node] = [Node() for _ in range(self.MAP_LEN)]

    def put(self, key: int, value: int) -> None:
        hashValue = self._calcHashValue(key)
        node = self._hashMap[hashValue]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        hashValue = self._calcHashValue(key)
        node = self._hashMap[hashValue].next
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        hashValue = self._calcHashValue(key)
        node = self._hashMap[hashValue]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def _calcHashValue(self, val: int) -> int:
        return val % len(self._hashMap)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)