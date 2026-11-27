class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = { course: [] for course in range(numCourses) }
        for p in prerequisites:
            prereqs[p[0]].append(p[1])

        visited = set()


        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if course not in prereqs:
                return True
            if not prereqs[course]:
                return True
            
            visited.add(course)
            for preCourse in prereqs[course]:
                if not dfs(preCourse):
                    return False
            visited.remove(course)
            prereqs[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True