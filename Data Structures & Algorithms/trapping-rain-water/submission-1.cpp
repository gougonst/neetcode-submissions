class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int l = 0, r = n - 1;
        int trappedWater = 0;
        while (l < r) {
            int nextL = l + 1;
            int nextR = r - 1;

            int accumWater = 0;
            while (nextL < r && height[nextL] < height[l]) {
                accumWater += height[l] - height[nextL];
                nextL++;
            }
            if (height[nextL] >= height[l]) {
                trappedWater += accumWater;
                l = nextL;
            }

            accumWater = 0;
            while (nextR > l && height[nextR] < height[r]) {
                accumWater += height[r] - height[nextR];
                nextR--;
            }
            if (height[nextR] >= height[r]) {
                trappedWater += accumWater;
                r = nextR;
            }
        }
        return trappedWater;
    }
};
