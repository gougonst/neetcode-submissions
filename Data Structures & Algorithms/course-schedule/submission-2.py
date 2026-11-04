class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = collections.defaultdict(list)
        for prerequisite in prerequisites:
            prerequisiteMap[prerequisite[0]].append(prerequisite[1])

        canFinished = set()

        def isCircular(course: int, visited: Set[int]) -> bool:
            # Handle canFinished, if the course can be finished, there is no circular for this course
            if course in canFinished:
                return False

            # Handle visited, if the course already visited, means encounter the circular
            if course in visited:
                return True

            # Handle leaf, leaf means there is no prerequisite
            if course not in prerequisiteMap:
                canFinished.add(course)
                return False

            visited.add(course)
            for prerequisite in prerequisiteMap[course]:
                if isCircular(prerequisite, visited):
                    return True
            canFinished.add(course)
            return False

        for course in prerequisiteMap.keys():
            visited = set()
            if isCircular(course, visited):
                return False
        return True