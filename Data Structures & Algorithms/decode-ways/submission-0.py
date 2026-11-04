class Solution:
    def numDecodings(self, s: str) -> int:
        # count: int
        # Crete a mapping table
        # DFS Algorithm:
        # Prefix: Fixed in current state.
        # i: Current index
        # End criteria: i > len(s)
        # For each character in s, I can choose whether use it or not
        #   If choose use i ~ j, it is invalid, return ""
        #   If it is valid, count + 1
        #     Do next dfs
        #   If not choose use i ~ j, keep track i ~ j + 1
        count = 0

        def dfs(prefix: str, start: int) -> None:
            nonlocal count

            if start == len(s):
                count += 1
                return
            if start > len(s):
                return

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if substr[0] == "0":
                    return
                if int(substr) < 1 or int(substr) > 26:
                    return
                dfs(prefix + chr(ord("A") + int(substr) - 1), end)

        dfs("", 0)
        return count