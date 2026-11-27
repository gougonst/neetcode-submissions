class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = { course: [] for course in range(numCourses) }
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            indegrees[child] += 1

        q = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)

        while q:
            qLen = len(q)
            for _ in range(qLen):
                parent = q.popleft()
                for child in graph[parent]:
                    indegrees[child] -= 1
                    if indegrees[child] != 0:
                        continue
                    q.append(child)

        for indegree in indegrees:
            if indegree != 0:
                return False
        return True