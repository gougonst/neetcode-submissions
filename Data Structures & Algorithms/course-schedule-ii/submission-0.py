class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i: [] for i in range(numCourses) }
        for prerequisite in prerequisites:
            preMap[prerequisite[0]].append(prerequisite[1])

        order = []
        visited = set()
        isFinished = set()

        def findLoop(course: int) -> bool:
            if course in visited:
                return True
            if course in isFinished:
                return False

            visited.add(course)
            for prerequisite in preMap.get(course, []):
                if findLoop(prerequisite):
                    return True
            order.append(course)
            visited.remove(course)
            preMap[course] = []
            isFinished.add(course)
            return False

        for course in range(numCourses):
            if findLoop(course):
                return []
        return order