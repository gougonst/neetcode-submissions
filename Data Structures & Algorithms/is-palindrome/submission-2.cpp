class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;

        while (l < r) {
            while (l < r && !validCharacter(s[l])) {
                l++;
            }
            while (r > l && !validCharacter(s[r])) {
                r--;
            }

            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    bool validCharacter(char c) {
        return isalpha(c) || isdigit(c);
    }
};
