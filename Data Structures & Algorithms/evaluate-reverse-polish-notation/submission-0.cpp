class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // (1 + 2) * (3 + 4)
        // 1, 2, +, 3, 4, +, *
        stack<int> s;
        for (auto& token: tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int first = s.top();
                s.pop();
                int second = s.top();
                s.pop();

                int res = 0;
                if (token == "+") {
                    res = first + second;
                } else if (token == "-") {
                    res = second - first;
                } else if (token == "*") {
                    res = first * second;
                } else {
                    res = second / first;
                }
                s.push(res);
            } else {
                s.push(stoi(token));
            }
        }
        return s.top();
    }
};
