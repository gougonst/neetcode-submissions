class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        pathStack = []

        i = 0

        def handleSlash(i: int) -> int:
            while i < n and path[i] == "/":
                i += 1
            return i

        def handleWord(i: int) -> int:
            end = i
            while end < n and path[end] != "/":
                end += 1
            pathStack.append(path[i:end])
            return end

        while i < n:
            if path[i] == '/':
                i = handleSlash(i)
            else:
                i = handleWord(i)
                lastPath = pathStack[-1]
                if lastPath == ".":
                    pathStack.pop()
                elif lastPath == "..":
                    pathStack.pop()
                    if pathStack:
                        pathStack.pop()

        res = ""
        for path in pathStack:
            res += "/" + path
        return "/" if not pathStack else res
