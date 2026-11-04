class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = Counter(tasks)
        
        # Use frequency as priority
        freqPQ = [-freq for freq in taskFreq.values()]
        heapq.heapify(freqPQ)

        # Start consume
        time = 0
        # waitingTask: [freq, time]
        waitingTasks = deque()
        while freqPQ or waitingTasks:
            time += 1
            if not freqPQ:
                time = waitingTasks[0][1]
            else:
                freq = 1 + heapq.heappop(freqPQ)
                if freq:
                    waitingTasks.append([freq, time + n])

            if waitingTasks and time == waitingTasks[0][1]:
                heapq.heappush(freqPQ, waitingTasks.popleft()[0])
        return time