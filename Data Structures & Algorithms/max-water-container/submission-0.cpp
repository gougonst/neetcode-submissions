class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int maxWater = 0;

        while (l < r) {
            int curWater = min(heights[l], heights[r]) * (r - l);
            maxWater = max(maxWater, curWater);

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxWater;
    }
};
