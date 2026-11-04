class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        int minimum = nums[0];
        while (l <= r) {
            int mid = l + (r - l) / 2;
            minimum = min(minimum, nums[mid]);

            if (nums[mid] < nums[0]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return minimum;
    }
};
