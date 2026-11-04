class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prerequisiteMap = collections.defaultdict(set)
        for prerequisite in prerequisites:
            prerequisiteMap[prerequisite[1]].add(prerequisite[0])
        
        courseMap = collections.defaultdict(set)

        def dfs(course: int) -> Set[int]:
            if course in courseMap:
                return courseMap[course]

            courseMap[course].add(course)
            for prerequisite in prerequisiteMap[course]:
                courseMap[course] |= dfs(prerequisite)
            return courseMap[course]

        for course in range(numCourses):
            courseMap[course] = dfs(course)

        res = []
        for query in queries:
            res.append(query[0] in courseMap[query[1]])
        return res