class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while (
                l < len(s)
                and not s[l].isdigit() 
                and not s[l].isalpha()
            ):
                l += 1

            while (
                r >= 0
                and not s[r].isdigit() 
                and not s[r].isalpha()
            ):
                r -= 1
            
            if (
                l < r 
                and s[l] != s[r]
            ):
                return False

            l += 1
            r -= 1
        return True