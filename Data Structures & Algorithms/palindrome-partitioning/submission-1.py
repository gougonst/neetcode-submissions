class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palindromes = []

        # Fill palindrome into palindromes
        def backtrack(palindrome: List[int], i: int) -> None:
            # Assume before index i, have already formed as palindromes
            # End criteria: i >= n
            if i == n:
                palindromes.append(palindrome.copy())
                return

            # From i, backtrack each palindrome possibility
            for j in range(i, n):
                if not Solution.isPalindrome(s[i:j + 1]):
                    continue
                palindrome.append(s[i:j + 1])
                backtrack(palindrome, j + 1)
                palindrome.pop()

        backtrack([], 0)
        return palindromes

    @staticmethod
    def isPalindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True