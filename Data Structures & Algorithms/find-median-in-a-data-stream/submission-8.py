class MedianFinder:

    def __init__(self):
        self.large = [] # min heap
        self.small = [] # max heap


    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -tmp)
        if len(self.small) > len(self.large) + 1:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -tmp)
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (self.large[0] + (-self.small[0])) / 2
        
        