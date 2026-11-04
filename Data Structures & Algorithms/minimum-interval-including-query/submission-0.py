class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        querySet = [(query, i) for i, query in enumerate(queries)]

        intervals.sort()
        querySet.sort()

        minLengths = [-1] * len(queries)
        iIdx = 0
        durationHeap = []
        for query, qIdx in querySet:
            while iIdx < len(intervals) and intervals[iIdx][0] <= query:
                duration = intervals[iIdx][1] - intervals[iIdx][0] + 1
                heapq.heappush(durationHeap, (duration, intervals[iIdx][1]))
                iIdx += 1

            while durationHeap and durationHeap[0][1] < query:
                heapq.heappop(durationHeap)
            
            if durationHeap:
                minLengths[qIdx] = durationHeap[0][0]
        return minLengths
