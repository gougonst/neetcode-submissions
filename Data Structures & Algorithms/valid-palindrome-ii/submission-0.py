class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validWithDeletion(deleteLeft: bool) -> bool:
            hasDeleted = False
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    continue
                    
                if hasDeleted:
                    return False

                if deleteLeft:
                    l += 1
                else:
                    r -= 1
                hasDeleted = True
            return True
        
        return validWithDeletion(True) or validWithDeletion(False)