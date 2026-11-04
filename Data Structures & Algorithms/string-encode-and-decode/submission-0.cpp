class Solution {
public:

    string encode(vector<string>& strs) {
        string encStr = "";
        for (auto& str: strs) {
            string lenStr = to_string(str.length());
            string lenLenStr = to_string(lenStr.length());
            encStr += str + lenStr + lenLenStr;
        }
        return encStr;
    }

    vector<string> decode(string s) {
        stack<string> decStrs;
        for (int i = s.length() - 1; i >= 0; i--) {
            int lenLenStr = s[i] - '0';
            int lenStr = atoi(s.substr(i - lenLenStr, lenLenStr).c_str());
            string str = s.substr(i - lenLenStr - lenStr, lenStr);
            decStrs.push(str);
            i -= lenLenStr + lenStr;
        }

        vector<string> ans;
        while (!decStrs.empty()) {
            ans.push_back(decStrs.top());
            decStrs.pop();
        }
        return ans;
    }
};
