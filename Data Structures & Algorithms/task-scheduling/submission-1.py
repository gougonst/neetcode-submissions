class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = {}
        for task in tasks:
            if task not in taskFreq:
                taskFreq[task] = 0
            taskFreq[task] += 1
        
        # Use frequency as priority
        taskPQ = []
        for task, freq in taskFreq.items():
            heapq.heappush(taskPQ, [-freq, task])

        # Start consume
        cycles = 0
        while taskPQ:
            taskRound = []
            for _ in range(n + 1):
                if not taskPQ:
                    break
                task = heapq.heappop(taskPQ)
                task[0] += 1
                taskRound.append(task)
            for task in taskRound:
                if task[0] != 0:
                    heapq.heappush(taskPQ, task)

            if taskPQ:
                cycles += n + 1
            else:
                cycles += len(taskRound)

        return cycles