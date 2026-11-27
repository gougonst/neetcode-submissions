class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs: defaultdict[int, set[int]] = defaultdict(set)
        graph: defaultdict[int, list[int]] = defaultdict(list)

        for prereq in prerequisites:
            prereqs[prereq[0]].add(prereq[1])
            graph[prereq[1]].append(prereq[0])

        q = deque()
        for course in range(numCourses):
            if course not in prereqs:
                q.append(course)

        while q:
            qLen = len(q)
            for _ in range(qLen):
                course = q.popleft()
                for child in graph[course]:
                    prereqs[child].remove(course)
                    if not prereqs[child]:
                        q.append(child)

        for prereq in prereqs.values():
            if prereq:
                return False
        return True