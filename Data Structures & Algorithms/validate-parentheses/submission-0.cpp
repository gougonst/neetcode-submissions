class Solution {
public:
    bool isValid(string s) {
        int n = s.size();

        stack<char> openBrackets;
        for (int i = 0; i < n; i++) {
            char bracket = s[i];
            if (_isOpenBracket(bracket)) {
                openBrackets.push(bracket);
            } else {
                if (openBrackets.empty()) {
                    return false;
                }
                char openBracket = openBrackets.top();
                openBrackets.pop();
                if (bracket == ')' && openBracket != '(' ||
                    bracket == ']' && openBracket != '[' ||
                    bracket == '}' && openBracket != '{') {
                    return false;
                }
            }
        }
        return openBrackets.empty();
    }
private:
    bool _isOpenBracket(char c) {
        return c == '(' || c == '[' || c == '{';
    }
};
