class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = { i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            prerequisiteMap[prerequisite[0]].append(prerequisite[1])

        visited = set()

        def isCircular(course: int) -> bool:
            if course in visited:
                return True
            if not prerequisiteMap.get(course, None):
                return False

            visited.add(course)
            for prerequisite in prerequisiteMap[course]:
                if isCircular(prerequisite):
                    return True
            visited.remove(course)
            return False

        for course in prerequisiteMap.keys():
            if isCircular(course):
                return False
        return True