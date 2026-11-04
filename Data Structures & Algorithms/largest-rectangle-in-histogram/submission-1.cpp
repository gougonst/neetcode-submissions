class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();

        stack<pair<int, int>> s;
        int largestArea = 0;

        for (int i = 0; i < n; i++) {
            int start = i;
            while (!s.empty() && s.top().second > heights[i]) {
                int index = s.top().first;
                int height = s.top().second;
                largestArea = max(largestArea, height * (i - index));

                s.pop();
                start = index;
            }
            s.push({start, heights[i]});
        }

        while (!s.empty()) {
            int index = s.top().first;
            int height = s.top().second;
            largestArea = max(largestArea, height * (n - index));
            s.pop();
        }

        return largestArea;
    }
};
