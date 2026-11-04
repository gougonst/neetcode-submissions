class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort the tasks by enqueue time
        n = len(tasks)
        sortedTasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])

        # Get the available tasks
        curTime, taskIdx = 0, 0

        availableTasks = []

        res = []

        while len(res) < n:
            # CPU is idling
            if not availableTasks and curTime < sortedTasks[taskIdx][0]:
                curTime = sortedTasks[taskIdx][0]

            # Put available tasks to heap with [Processing time, Index]
            while taskIdx < n and sortedTasks[taskIdx][0] <= curTime:
                _, processingTime, index = sortedTasks[taskIdx]
                heapq.heappush(availableTasks, (processingTime, index))
                taskIdx += 1

            # Process a task
            processingTime, index = heapq.heappop(availableTasks)
            curTime += processingTime
            res.append(index)

        return res

# Variable: Current time

# Steps:
# 1. Pop the available tasks
#     - Enqueue time <= Current time
# 2. Choose the top priority task
#     a. Shortest processing time
#     b. Smaller index
# 3. Execute the task, update the current time
#     - Current time = current time + processing time
# 4. Return to 1. until there is no available tasks
