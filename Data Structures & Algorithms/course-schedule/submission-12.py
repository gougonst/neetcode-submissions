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

        completed = 0

        while q:
            parent = q.popleft()
            completed += 1
            for child in graph[parent]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)

        return completed == numCourses