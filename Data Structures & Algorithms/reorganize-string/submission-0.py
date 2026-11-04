class Solution:
    def reorganizeString(self, s: str) -> str:
        freqHeap = []
        counter = Counter(s)
        for c, freq in counter.items():
            heapq.heappush(freqHeap, (-freq, c))

        res = ""
        while len(freqHeap) >= 2:
            firstFreq, firstChar = heapq.heappop(freqHeap)
            secondFreq, secondChar = heapq.heappop(freqHeap)
            res += firstChar + secondChar
            
            if -firstFreq > 1:
                heapq.heappush(freqHeap, (firstFreq + 1, firstChar))
            if -secondFreq > 1:
                heapq.heappush(freqHeap, (secondFreq + 1, secondChar))

        if freqHeap:
            if -freqHeap[0][0] > 1:
                return ""
            else:
                res += freqHeap[0][1]
        return res

        