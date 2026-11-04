class Node:
    def __init__(self, val: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self) -> int:
        return len(self.map)

    def pushRight(self, val: int) -> None:
        node = Node(val)
        self.map[val] = node

        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def pop(self, val: int) -> None:
        if val not in self.map:
            return
        node = self.map[val]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del self.map[val]

    def popLeft(self) -> int:
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val: int) -> None:
        self.pop(val)
        self.pushRight(val)
        


class LFUCache:

    def __init__(self, capacity: int):
        self.countMap = defaultdict(int) # { key: count }
        self.valMap = defaultdict(int) # { key: value }
        self.lruMap = defaultdict(DoublyLinkedList) # { count: LRU cache }
        self.capacity = capacity
        self.lfuCount = 0

    def counter(self, key) -> int:
        count = self.countMap[key]
        self.countMap[key] += 1
        self.lruMap[count].pop(key)
        self.lruMap[count + 1].pushRight(key)

        if count == self.lfuCount and self.lruMap[count].length() == 0:
            self.lfuCount += 1

    def get(self, key: int) -> int:
        if key not in self.countMap:
            return -1
        
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.countMap and len(self.countMap) == self.capacity:
            delKey = self.lruMap[self.lfuCount].popLeft()
            del self.countMap[delKey]
            del self.valMap[delKey]

        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)