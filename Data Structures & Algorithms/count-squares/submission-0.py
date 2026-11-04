class CountSquares:

    def __init__(self):
        # 3d dict, (y, x, count)
        self._points = collections.defaultdict(
            lambda: collections.defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self._points[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]

        totalCount = 0
        for candidateX, count in self._points[y].items():
            if x == candidateX:
                continue
            sideLength = abs(candidateX - x)

            # top
            totalCount += (count * 
                           self._points[y + sideLength][candidateX] *
                           self._points[y + sideLength][x])

            # bottom
            totalCount += (count * 
                           self._points[y - sideLength][candidateX] *
                           self._points[y - sideLength][x])

        return totalCount
