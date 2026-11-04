class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        if self.larger and num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)

        while len(self.larger) > len(self.smaller):
            tmp = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -tmp)
        while len(self.smaller) - len(self.larger) > 1:
            tmp = heapq.heappop(self.smaller)
            heapq.heappush(self.larger, -tmp)

    def findMedian(self) -> float:
        total = len(self.smaller) + len(self.larger)
        if total % 2 == 1:
            return -self.smaller[0]
        else:
            return (-self.smaller[0] + self.larger[0]) / 2
