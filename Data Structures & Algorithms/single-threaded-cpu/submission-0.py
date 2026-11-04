class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort the tasks by enqueue time
        sortedTasks = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        sortedTasks = collections.deque(sorted(sortedTasks, key=lambda item: item[0]))

        # Get the available tasks
        curTime = 0

        availableTasks = []

        res = []

        while sortedTasks or availableTasks:
            # CPU is idling
            if not availableTasks and curTime < sortedTasks[0][0]:
                curTime = sortedTasks[0][0]

            # Put available tasks to heap with [Processing time, Index]
            while sortedTasks and sortedTasks[0][0] <= curTime:
                task = sortedTasks.popleft()
                processingTime, index = task[1], task[2]
                heapq.heappush(availableTasks, [processingTime, index])

            # Process a task
            curTask = heapq.heappop(availableTasks)
            curTime += curTask[0]
            res.append(curTask[1])

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
