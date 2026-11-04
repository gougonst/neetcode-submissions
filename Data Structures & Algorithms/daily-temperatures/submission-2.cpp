class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> futureWarmers(n, 0);
        stack<pair<int, int>> lowers;

        for (int i = 0; i < n; i++) {
            int curTemp = temperatures[i];
            while (!lowers.empty() && curTemp > lowers.top().first) {
                pair<int, int> lower = lowers.top();
                lowers.pop();
                futureWarmers[lower.second] = i - lower.second;
            }
            lowers.push({curTemp, i});
        }
        return futureWarmers;
    }
};
