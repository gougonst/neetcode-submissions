class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string stack;

        backtrace(0, 0, n, res, stack);
        return res;
    }

    void backtrace(int openN, int closedN, int n, vector<string>& res, string& stack) {
        if (openN == closedN && openN == n) {
            res.push_back(stack);
            return;
        }

        if (openN < n) {
            stack += '(';
            backtrace(openN + 1, closedN, n, res, stack);
            stack.pop_back();
        }
        if (closedN < openN) {
            stack += ')';
            backtrace(openN, closedN + 1, n, res, stack);
            stack.pop_back();
        }
    }
};
