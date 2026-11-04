class TimeMap:

    def __init__(self):
        self._time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._time_map:
            self._time_map[key] = []
        self._time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._time_map or self._time_map[key][0][0] > timestamp:
            return ""

        # Here we can use binary search because the `set` function is
        # strictly increase the timestamp.
        time_values = self._time_map[key]
        l = 0
        r = len(time_values) - 1
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if timestamp < time_values[m][0]:
                r = m - 1
            else:
                l = m + 1
                res = m
        
        return time_values[res][1]
        
