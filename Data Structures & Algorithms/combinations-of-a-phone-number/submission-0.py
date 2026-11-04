class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitCharMap = {
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"], 
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"]
        }
        n = len(digits)
        combinations = []

        # Fill in the combinations
        def dfs(combination: str, i: int) -> None:
            # End criteria: i >= n, push the combination into result
            if i >= n:
                combinations.append(combination)
                return

            # At i position, choose each possibility
            for char in digitCharMap[digits[i]]:
                dfs(combination + char, i + 1)


        dfs("", 0)
        return combinations